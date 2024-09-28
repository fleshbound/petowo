import redis

from core.animal.service.impl.animal import AnimalService
from core.auth.service.impl.auth import AuthService
from core.breed.service.impl.breed import BreedService
from core.certificate.service.impl.certificate import CertificateService
from core.group.service.impl.group import GroupService
from core.show.service.impl.animalshow import AnimalShowService
from core.show.service.impl.score import ScoreService
from core.show.service.impl.show import ShowService
from core.show.service.impl.usershow import UserShowService
from core.species.service.impl.species import SpeciesService
from core.standard.service.impl.standard import StandardService
from core.user.service.impl.user import UserService
from dependency_injector import containers, providers
from repository.sqlalchemy.animal import SqlAlchemyAnimalRepository
from repository.sqlalchemy.animalshow import SqlAlchemyAnimalShowRepository
from repository.sqlalchemy.breed import SqlAlchemyBreedRepository
from repository.sqlalchemy.certificate import SqlAlchemyCertificateRepository
from repository.sqlalchemy.group import SqlAlchemyGroupRepository
from repository.sqlalchemy.score import SqlAlchemyScoreRepository
from repository.sqlalchemy.show import SqlAlchemyShowRepository
from repository.sqlalchemy.species import SqlAlchemySpeciesRepository
from repository.sqlalchemy.standard import SqlAlchemyStandardRepository
from repository.sqlalchemy.user import SqlAlchemyUserRepository
from repository.sqlalchemy.usershow import SqlAlchemyUserShowRepository
from auth_provider.provider.auth import AuthProvider
from auth_provider.storage.redis.auth import SessionStorage
from config import configs
from repository.database.database import SqlAlchemyDatabase
from tech.console import ConsoleHandler
from tech.handlers.service.animal import ServiceAnimalHandler
from tech.handlers.service.auth import ServiceAuthHandler
from tech.handlers.service.input import StdIOInputHandler
from tech.handlers.service.show import ServiceShowHandler
from tech.utils.lang.impl.rulang import RuLanguageModel


def redis_client():
    return redis.Redis(host=configs.REDIS_HOST,
                       port=int(configs.REDIS_PORT))
                       # password=configs.REDIS_USER_PASSWORD,
                       # db=configs.REDIS_DB,
                       # username=configs.REDIS_USER)


class Container(containers.DeclarativeContainer):
    db = providers.Singleton(SqlAlchemyDatabase, db_url=configs.DATABASE_URL, echo=False)

    user_repo = providers.Factory(SqlAlchemyUserRepository, session_factory=db.provided.session)
    user_service = providers.Factory(UserService, user_repo=user_repo)

    breed_repo = providers.Factory(SqlAlchemyBreedRepository, session_factory=db.provided.session)
    breed_service = providers.Factory(BreedService, breed_repo=breed_repo)

    species_repo = providers.Factory(SqlAlchemySpeciesRepository, session_factory=db.provided.session)
    species_service = providers.Factory(SpeciesService, species_repo=species_repo)

    group_repo = providers.Factory(SqlAlchemyGroupRepository, session_factory=db.provided.session)
    group_service = providers.Factory(GroupService, group_repo=group_repo)

    certificate_repo = providers.Factory(SqlAlchemyCertificateRepository, session_factory=db.provided.session)
    certificate_service = providers.Factory(CertificateService, certificate_repo=certificate_repo)

    animalshow_repo = providers.Factory(SqlAlchemyAnimalShowRepository, session_factory=db.provided.session)
    animalshow_service = providers.Factory(AnimalShowService, animalshow_repo=animalshow_repo)

    usershow_repo = providers.Factory(SqlAlchemyUserShowRepository, session_factory=db.provided.session)
    usershow_service = providers.Factory(UserShowService, usershow_repo=usershow_repo)

    standard_repo = providers.Factory(SqlAlchemyStandardRepository, session_factory=db.provided.session)
    standard_service = providers.Factory(StandardService, standard_repo=standard_repo)

    show_repo = providers.Factory(SqlAlchemyShowRepository, session_factory=db.provided.session)
    animal_repo = providers.Factory(SqlAlchemyAnimalRepository, session_factory=db.provided.session)
    animal_service = providers.Factory(AnimalService,
                                       animal_repo=animal_repo,
                                       animalshow_service=animalshow_service,
                                       show_repo=show_repo)
    score_repo = providers.Factory(SqlAlchemyScoreRepository, session_factory=db.provided.session)
    score_service = providers.Factory(
        ScoreService,
        score_repo=score_repo,
        animal_service=animal_service,
        animalshow_service=animalshow_service,
        usershow_service=usershow_service
    )
    show_service = providers.Factory(
        ShowService,
        show_repo=show_repo,
        score_service=score_service,
        animalshow_service=animalshow_service,
        usershow_service=usershow_service,
        certificate_service=certificate_service,
        animal_service=animal_service,
        user_service=user_service,
        breed_service=breed_service,
        standard_service=standard_service
    )

    auth_storage = providers.Singleton(SessionStorage, redis_client=providers.Callable(redis_client))
    auth_provider = providers.Factory(AuthProvider, config=configs.auth_config, session_storage=auth_storage)
    auth_service = providers.Factory(AuthService, user_service=user_service, auth_provider=auth_provider)

    lang_model = providers.Singleton(RuLanguageModel)
    input_handler = providers.Factory(StdIOInputHandler, lang_model=lang_model)
    animal_handler = providers.Factory(ServiceAnimalHandler, animal_service=animal_service, show_service=show_service,
                                       input_handler=input_handler)
    show_handler = providers.Factory(ServiceShowHandler,
                                     show_service=show_service,
                                     usershow_service=usershow_service,
                                     score_service=score_service,
                                     input_handler=input_handler,
                                     animalshow_service=animalshow_service,
                                     animal_service=animal_service)
    auth_handler = providers.Factory(ServiceAuthHandler, auth_service=auth_service, user_service=user_service,
                                     input_handler=input_handler)
    console_handler = providers.Factory(ConsoleHandler, animal_handler=animal_handler,
                 show_handler=show_handler,
                 auth_handler=auth_handler,
                 input_handler=input_handler)
