import os
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key=os.environ.get('GROQ_API_KEY'),
    model_name="llama-3.1-70b-versatile",
)


def conduct_interview(initial_question):
    conversation_history = [
        {"role": "system", "content": "You are an interviewer conducting a technical interview."}]

    conversation_history.append(
        {"role": "assistant", "content": initial_question})

    while True:
        print(f"Question: {initial_question}")

        user_answer = input("Your answer (type 'exit' to finish): ")

        if user_answer.lower() == 'exit':
            print("Thank you for participating in the interview!")
            break

        conversation_history.append({"role": "user", "content": user_answer})

        response = llm.invoke(conversation_history)

        new_question = response.content

        initial_question = new_question

        conversation_history.append(
            {"role": "assistant", "content": new_question})


if __name__ == "__main__":
    initial_question = "Tell me about yourself."
    conduct_interview(initial_question)
