from typing import List, Optional

from sqlalchemy import text

from src.domain.commons.exceptions import QuestaoNotFoundException
from src.domain.models.dto.filtro_questao_request import FiltroQuestaoRequest
from src.domain.models.questao import Questao
from src.domain.models.repositories.questao_repository import QuestaoRepository
from src.infrastructure.db.connection import Session
from src.infrastructure.db.entities.questao_entity import QuestaoEntity


class QuestaoRepositoryDbImpl(QuestaoRepository):

    def obter_por_filtro(self, filtro: FiltroQuestaoRequest) -> List[Questao]:
        session = Session()
        query = session.query(QuestaoEntity)
        # montando query dinâmica
        if filtro.tipo:
            query = query.filter(QuestaoEntity.tipo == filtro.tipo.name)
        if filtro.disciplina:
            query = query.filter(QuestaoEntity.disciplina == filtro.disciplina.name)
        if filtro.ano:
            query = query.filter(QuestaoEntity.ano == filtro.ano)
        if filtro.instituicao:
            query = query.filter(QuestaoEntity.instituicao == filtro.instituicao)
        if filtro.origem:
            query = query.filter(QuestaoEntity.origem == filtro.origem.name)
        query = query.filter(QuestaoEntity.ativo == True)
        # executando a query
        questoes = query.all()
        return list(map(lambda q: q.to_model(), questoes))

    def obter_por_codigo(self, codigo: int) -> Optional[Questao]:
        session = Session()
        questao = session.query(QuestaoEntity).filter(QuestaoEntity.id == codigo).first()
        if questao:
            return questao.to_model()
        return None

    def obter_proxima_questao(self, codigo: int) -> Optional[Questao]:
        session = Session()
        questao = (session.query(QuestaoEntity)
                   .filter(QuestaoEntity.tipo == "MULTIPLA_ESCOLHA")
                   .filter(QuestaoEntity.id > codigo).first())
        if questao:
            return questao.to_model()
        return None

    def obter_todos(self) -> List[Questao]:
        session = Session()
        questoes = session.query(QuestaoEntity).filter(QuestaoEntity.ativo == True)
        return list(map(lambda q: q.to_model(), questoes))

    def salvar(self, questao: Questao) -> Questao:
        session = Session()
        questao_entity = QuestaoEntity(questao)
        session.add(questao_entity)
        session.commit()
        for assunto in questao.assuntos:
            query = text(
                "INSERT INTO questao_assunto (questao_id, assunto_id) VALUES (" + str(questao_entity.id) + ", " + str(
                    assunto.codigo) + ")")
            session.execute(query)
        session.commit()
        return questao_entity.to_model()

    def excluir_questao(self, codigo: int) -> bool:
        session = Session()
        questao = session.query(QuestaoEntity).filter(QuestaoEntity.id == codigo).first()
        if questao:
            questao.ativo = False
            session.commit()
            return True
        else:
            raise QuestaoNotFoundException(codigo)
