from dotenv import load_dotenv
import os
load_dotenv()
def main():
    print("Hello from langchain-course-1!")
    print(os.environ.get("OPEN_API_KEY"))


if __name__ == "__main__":
    main()
