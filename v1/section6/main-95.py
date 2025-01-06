# 多重継承を使う
from abc import ABC, abstractmethod

# 講師も生徒も視聴可能
class Course(ABC):
    # 共通のメソッド
    @abstractmethod
    def view_lecture(self) -> None:
        pass

#　講師用と生徒用にそれぞれインターフェースを用意する
class InstructorCourseInterface(ABC):
    @abstractmethod
    def add_lecture(self, content_name: str) -> None:
        pass

class StudentCourseInterface(ABC):
    @abstractmethod
    def review_course(self) -> None:
        pass

# 多重継承して必要な機能だけを用意する
class CourseFromInstructors(Course, InstructorCourseInterface):
    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 講師用の動画再生の処理

    def add_lecture(self, content_name: str) -> None:
        # レクチャー作成処理
        print(f'新規レクチャー「{content_name}」を作成しました')

class CourseFromStudents(Course, StudentCourseInterface):
    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 生徒用の動画再生の処理

    def review_course(self) -> None:
        print('コースのレビューをおねがいします')
        # レビューの投稿処理