import datetime
import traceback

from sqlalchemy import Column, Integer, Numeric, String, DateTime
from sqlalchemy.dialects.mysql import TINYINT

from models import Base, session


class AiAnalysisLog(Base):

    __tablename__ = 'ai_analysis_log'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    image_path = Column('image_path', String(255), nullable=True)
    success = Column('success', TINYINT, nullable=False)
    message = Column('message', String(255), nullable=True)
    assigned_class = Column('class', Integer, nullable=True)
    confidence = Column('confidence', Numeric(5, 4), nullable=True)
    request_timestamp = Column('request_timestamp', DateTime, nullable=True)
    response_timestamp = Column('response_timestamp', DateTime, nullable=True)

    @staticmethod
    def register_data(
        success: str,
        image_path: int,
        message: str,
        assigned_class: int,
        confidence: float,
        request_time: datetime,
        response_time: datetime
    ) -> bool:
        '''
        ai_analysis_logテーブルにデータを登録する

        param:
            image_path <str> 画像ファイルのパス
            success <int> 1: 成功 2: 失敗
            message <str> メッセージ
            assigned_class <int> クラス
            confidence <float> 信頼性
            request_time <datetime> APIリクエスト時間
            response_time <datetime> APIレスポンス時間
        return:
            bool True: 登録成功 False: 登録失敗
        '''
        try:
            session.add(
                AiAnalysisLog(
                    success=success,
                    image_path=image_path,
                    message=message,
                    assigned_class=assigned_class,
                    confidence=confidence,
                    request_timestamp=request_time,
                    response_timestamp=response_time
                )
            )
            session.commit()
            return True
        except Exception:
            traceback.format_exc()
            return False
