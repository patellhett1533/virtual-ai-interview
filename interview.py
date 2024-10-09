import speech_recognition as sr
import pyttsx3
import gtts
import playsound
from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.1-70b-versatile",
)


def check_score_accuracy(question, user_answer):
    reponse = llm.invoke(
        """
        this is a question "{question}" and user submit this answer "{user_answer}", so please tell me that how user answer is accurate logically and score. give only score number formate only
        """)
    return reponse.content


def get_user_answer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."


def speak_question(question):
    sound = gtts.gTTS(question, lang="en")
    sound.save("myaudio.mp3")
    playsound.playsound("myaudio.mp3")


if __name__ == "__main__":
    question = "What is the difference between let, const, and var in JavaScript?"
    speak_question(question)

    user_answer = get_user_answer()

    score = check_score_accuracy(question, user_answer)
    print(score)
