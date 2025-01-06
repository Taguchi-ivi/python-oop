# ISPに違反しているコード
# それぞれ専用のメソッド(講師、生徒専用メソッド)が不要なのに依存してしまっている
# 処理自体は書かず、passとしているが違反している
from abc import ABC, abstractmethod

class Course(ABC):
    # 共通のメソッド
    @abstractmethod
    def view_lecture(self) -> None:
        pass

    # 講師専用のメソッド
    @abstractmethod
    def add_lecture(self, content_name: str) -> None:
        pass

    # 生徒専用のメソッド
    @abstractmethod
    def review_course(self) -> None:
        pass

class CourseFromInstructors(Course):
    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 講師用の動画再生の処理

    def add_lecture(self, content_name: str) -> None:
        # レクチャー作成処理
        print(f'新規レクチャー「{content_name}」を作成しました')

    def review_course(self) -> None:
        pass # 講師はレビュー出来ないので実装しない

class CourseFromStudents(Course):
    def view_lecture(self) -> None:
        print('視聴を開始します')
        # 生徒用の動画再生の処理

    def add_lecture(self, content_name: str) -> None:
        pass # 生徒はレクチャーを追加出来ないので実装しない

    def review_course(self) -> None:
        print('コースのレビューをおねがいします')
        # レビューの投稿処理