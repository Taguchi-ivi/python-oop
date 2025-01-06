# 承継とコンポジションを組み合わせる
# それぞれ必要な抽象クラスをコンストラクタで定義
from abc import ABC, abstractmethod

# 共通のインターフェース
class Course(ABC):
    @abstractmethod
    def view_lecture(self) -> None:
        pass

class InstructorBehaviour:
    def add_lecture(self, content_name: str) -> None:
        print(f'新規レクチャー「{content_name}」を作成しました')

class StudentBehaviour:
    def review_course(self) -> None:
        print('コースのレビューをおねがいします')

class CourseFromInstructors(Course):
    def __init__(self) -> None:
        self.instructor_behaviour = InstructorBehaviour()

    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 講師用の動画再生の処理

    def add_lecture(self, content_name: str) -> None:
        self.instructor_behaviour.add_lecture(content_name)

class CourseFromStudents(Course):
    def __init__(self) -> None:
        self.student_behaviour = StudentBehaviour()

    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 生徒用の動画再生の処理

    def review_course(self) -> None:
        self.student_behaviour.review_course()