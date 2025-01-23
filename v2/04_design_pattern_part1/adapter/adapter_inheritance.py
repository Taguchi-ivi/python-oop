from abc import ABC, abstractmethod

class Target(ABC):
    @abstractmethod
    def get_csv_data(self) -> str:
        pass


class NewLibrary:
    def get_json_data(self) -> list[dict[str, str]]:
        return [
            {
                "data1": "json_dataA",
                "data2": "json_dataB",
            },
            {
                "data1": "json_dataC",
                "data2": "json_dataD",
            },
        ]


# 多重継承によって、本来clientが利用できなかったNewLibraryのget_json_dataメソッドを利用できるようにする
class JsonToCsvAdapter(Target, NewLibrary):
    def get_csv_data(self) -> str:
        json_data = self.get_json_data()

        header = ",".join(json_data[0].keys()) + "\n"
        body = "\n".join([",".join(data.values()) for data in json_data])
        return header + body


if __name__ == "__main__":
    adaptee = NewLibrary()
    print("Adaptee: ", adaptee.get_json_data())
    print("")

    adapter = JsonToCsvAdapter()
    print("Adapter: ", adapter.get_csv_data())
