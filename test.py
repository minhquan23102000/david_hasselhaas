from haas.tools.list_directory import ListDirectory
from haas.tools.web_retrieve import WebRetrieve

if __name__ == "__main__":
    # print(ListDirectory().do_it("./"))
    print(
        WebRetrieve().do_it(
            "https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file"
        )
    )
