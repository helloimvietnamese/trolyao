import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser as wb
import requests

# Khởi tạo các đối tượng cho việc nhận dạng giọng nói và nói ra
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

# Hàm để tìm kiếm trên Wikipedia
def search_wikipedia(query):
    # Thay thế các khoảng trắng trong truy vấn bằng dấu cộng (+)
    query = query.replace(" ", "+")
    # Gửi yêu cầu tìm kiếm đến API của Wikipedia
    response = requests.get(f"https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch={query}")
    
    # Xử lý kết quả trả về
    if response.status_code == 200:
        data = response.json()
        search_results = data['query']['search']
        # Lấy ra kết quả đầu tiên
        if search_results:
            title = search_results[0]['title']
            snippet = search_results[0]['snippet']
            url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
            return title, snippet, url
    return None, None, None

# Hàm để đọc văn bản bằng giọng nói
def speak(text):
    robot_mouth.say(text)
    robot_mouth.runAndWait()

# Vòng lặp chính của chương trình
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""

    print("you: " + you)

    # Xử lý các lệnh từ người dùng
    if you == "":
        robot_brain = "Can you speak again, I can't hear anything"   
    elif "hello" in you:
        robot_brain = " Hello. How cam i help you" 
    elif "oh" in you:
        robot_brain = "hehehe"
    elif "your name" in you:
        robot_brain = "OH .My name is Kevin"        
    elif "day" in you:
        today = date.today() 
        robot_brain = today.strftime("%B %d, %Y") 
    elif "time" in you:
        now = datetime.now() 
        robot_brain = now.strftime("%H hours %M minutes %S seconds %p")
    elif "president of america" and "President of america" and "president of America" in you:
        robot_brain = "it's Joe Biden"
    elif "President of Vietnam" in you:
        robot_brain = "it's Phạm Minh Chính"
    elif "your name" in you: 
        robot_brain = "My name is Kevin assistant" 
    elif " joke story" in you: 
        robot_brain = "Mom, is the Pacific Ocean always peaceful? Can I ask you anything more intelligent? It's OK. So it's called Africa because there are a lot of… Buffaloes roam like horses, right?.                  translate that sentence into Vietnamese😂😂😂🤣🤣🤣🤣"
    elif "scary story" in you:
        robot_brain = "My grandfather told me this story about how one time he was sitting in a chair in front of the house, when he heard his wife repeatedly calling him from inside the house. The thing is, my grandmother passed away a few years before that. But he told me that the voice was so pressing that he actually got up to look inside the house, and as soon as he got inside he heard a loud crash behind him and turned around to see that the chair he has been sitting in moments ago had been crushed by the cast iron gutter that fell on it. If he hadn't come inside the house he would have probably been seriously injured. I don't know if it's paranormal or not, but every time I think about it it sends chills down my spine."
    elif "not funny" in you:
        robot_brain = "sorry"
    elif "Google" in you:
        robot_brain = "OK, mở Google. what do you want to search?"
        speak(robot_brain)
        print("Robot: " + robot_brain)
        with speech_recognition.Mic-rophone() as mic:
            print("Robot: I'm listening")
            audio = robot_ear.listen(mic)
        print("Robot: ...")

        try:
            query = robot_ear.recognize_google(audio)
            robot_brain = f"Searching for {query} on Google."
            wb.open_new_tab(f"https://www.google.com/search?q={query}")
        except:
            robot_brain = "Sorry, I couldn't understand your search query."
    elif "YouTube" in you:
        robot_brain = "OK"
        url = f"https://www.youtube.com/"
        wb.open(url)
        robot_brain = "Here is youtube"
    elif "Facebook" in you:
        robot_brain = "OK"
        url = f"https://www.facebook.com/"
        wb.open(url)
        robot_brain = "Here is facebook"
    elif "Wikipedia" in you:
        search_query = you.replace("Wikipedia", "").strip()
        title, snippet, url = search_wikipedia(search_query)
        if title:
            robot_brain = f"Here is what I found on Wikipedia: {title}. {snippet}"
            wb.open(url)
        else:
            robot_brain = "Sorry, I couldn't find any relevant information on Wikipedia."
    elif "bye" in you: 
        robot_brain = "bye Kevin" 
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else: 
        robot_brain = "Sorry, I'm not smart enough to understand"

    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    