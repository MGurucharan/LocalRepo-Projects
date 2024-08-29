import time
import playsound
import random 
import threading

incoming=r"C:\Users\mguru\Downloads\kbc-question.mp3"
intro=r"C:\Users\mguru\Downloads\intro.mp3"
wrongans=r"C:\Users\mguru\Downloads\10. Wrong Answer.mp3"
special=r"C:\Users\mguru\Downloads\7crore.mp3"
timer3=r"C:\Users\mguru\Downloads\timerfr.mp3"
correctans=r"C:\Users\mguru\Downloads\correctans.mp3"
lock=r"C:\Users\mguru\Downloads\lock.mp3"
crore7intro=r"C:\Users\mguru\Downloads\crore7intro.mp3"

question_bank= [
    ["Who was the first President of India?", "Dr. Rajendra Prasad", "Dr. S. Radhakrishnan", "Zakir Hussain", "V. V. Giri", 1],
    ["Which is the longest river in India?", "Ganges", "Yamuna", "Godavari", "Brahmaputra", 1],
    ["Who wrote the national anthem of India?", "Bankim Chandra Chattopadhyay", "Rabindranath Tagore", "Sarojini Naidu", "Mahatma Gandhi", 2],
    ["Which is the smallest state in India by area?", "Goa", "Sikkim", "Tripura", "Manipur", 1],
    ["What is the capital of Karnataka?", "Chennai", "Bangalore", "Hyderabad", "Mumbai", 2],
    ["Who is known as the 'Iron Man of India'?", "Jawaharlal Nehru", "Mahatma Gandhi", "Subhas Chandra Bose", "Sardar Vallabhbhai Patel", 4],
    ["In which year did India gain independence?", "1945", "1947", "1948", "1950", 2],
    ["Who is the author of the book 'Discovery of India'?", "Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Sardar Vallabhbhai Patel", 2],
    ["Which Indian city is also known as the 'Silicon Valley of India'?", "Mumbai", "Hyderabad", "Bangalore", "Pune", 3],
    ["Which Mughal emperor built the Taj Mahal?", "Akbar", "Shah Jahan", "Aurangzeb", "Jahangir", 2],
    ["What is the national animal of India?", "Lion", "Elephant", "Tiger", "Peacock", 3],
    ["Who was the first Indian woman in space?", "Kalpana Chawla", "Sunita Williams", "Indira Gandhi", "Rani Lakshmibai", 1],
    ["Which sport is associated with the term 'Duck'?", "Hockey", "Cricket", "Football", "Badminton", 2],
    ["Who invented the zero?", "Aryabhata", "Bhaskara I", "Brahmagupta", "Ramanujan", 1],
    ["Which Indian classical dance form is from Kerala?", "Bharatanatyam", "Kathakali", "Odissi", "Manipuri", 2],
    ["Who is the chairman of the Indian Space Research Organisation (ISRO) as of 2023?", "K. Sivan", "A. S. Kiran Kumar", "S. Somanath", "G. Madhavan Nair", 3],
    ["Which Indian state has the longest coastline?", "Gujarat", "Tamil Nadu", "Maharashtra", "Andhra Pradesh", 1],
    ["Who was the first recipient of the Bharat Ratna?", "C. Rajagopalachari", "S. Radhakrishnan", "C. V. Raman", "Jawaharlal Nehru", 1],
    ["What is the national flower of India?", "Rose", "Lotus", "Marigold", "Sunflower", 2],
    ["Which city is known as the 'City of Joy'?", "Mumbai", "Delhi", "Chennai", "Kolkata", 4],
    ["Which is the highest civilian award in India?", "Padma Shri", "Padma Bhushan", "Padma Vibhushan", "Bharat Ratna", 4],
    ["Who is the father of the Indian Constitution?", "Mahatma Gandhi", "Jawaharlal Nehru", "Dr. B.R. Ambedkar", "Rajendra Prasad", 3],
    ["What is the currency of India?", "Dollar", "Euro", "Rupee", "Pound", 3],
    ["Which Indian state is known as the 'Spice Garden of India'?", "Kerala", "Tamil Nadu", "Karnataka", "Andhra Pradesh", 1],
    ["Who is the author of the 'Ramayana'?", "Ved Vyasa", "Valmiki", "Tulsidas", "Kalidasa", 2],
    ["Which Indian leader was known as the 'Nightingale of India'?", "Sarojini Naidu", "Indira Gandhi", "Mother Teresa", "Annie Besant", 1],
    ["Who won the first Olympic medal for India?", "Milkha Singh", "P.T. Usha", "Abhinav Bindra", "K.D. Jadhav", 4],
    ["What is the national tree of India?", "Banyan", "Neem", "Peepal", "Mango", 1],
    ["Which Indian festival is known as the 'Festival of Lights'?", "Holi", "Diwali", "Eid", "Christmas", 2],
    ["Who was the first woman Prime Minister of India?", "Indira Gandhi", "Sarojini Naidu", "Pratibha Patil", "Sushma Swaraj", 1]
]
# No repetition and SHUFFLED
random_questions=[]
random.shuffle(question_bank)
for question in question_bank:
     random.shuffle(question_bank) #TO CREATE MORE RANDOMNESS 
     if question not in random_questions:
          random_questions.append(question)
     if len(random_questions)==16:
          break
     else:
          continue

print('''\n\n                     ********************** WELCOME TO KAUN BANEGA CROREPATI SEASON 1 *******************
                     **********************    RULES : 10 SECONDS EACH QUESTION       *******************
                     **********************   CHECKPOINTS AT 10,000 ₹ AND 3,20,000 ₹  *******************
                     **********************              GOOD LUCK ! ! !              *******************      
''')
print("\nThe Question bank is",random_questions)
print(len(random_questions))
levels=['1000 ₹','2000 ₹','3000 ₹','5000 ₹','10,000 ₹','20,000 ₹','40,000 ₹','80,000 ₹','1,60,000 ₹','3,20,000 ₹','6,40,000 ₹','12,50,000 ₹','25,00,000 ₹','50,00,000 ₹','1,00,00,000 ₹','7,00,00,000 ₹']
money=0
playsound.playsound(intro)
for i in range(16): # 0 1 2 3 4 5 6 ......15
        print(f"Question for {levels[i]}\n")
        time.sleep(1) #delay 1 sec
        playsound.playsound(incoming)
        print(random_questions[i][0])
        print(f"a.{random_questions[i][1]}         b.{random_questions[i][2]}")
        print(f"c.{random_questions[i][3]}         d.{random_questions[i][4]}")
        def play_sound(x):
          playsound.playsound(x)
        def countdown_timer():

          #Running the background timer sound using threads

          sound_thread = threading.Thread(target=play_sound, args=(timer3,))
          sound_thread.start() #starts the thread to execute in the background 

          #Displaying the dynamic timer :
          print("\nTimer ticking :   ",end='')
          for second in range(10,-1,-1):
               print(f"\b\b\b{second:3d}",end='')
               time.sleep(2)
          print("\nTime's up !!!")

        countdown_timer()

        res=int(input("Enter (1-4) or 0 to quit: "))
        if res==0:
          print("Your take home money is",levels[i-1])
          break
        else:
          playsound.playsound(lock)
          if res==random_questions[i][-1]: #correct answer
               playsound.playsound(correctans)
               if(levels[i]=='7,00,00,000 ₹'):
                    playsound.playsound(special)
                    playsound.playsound(crore7intro)
               print(f"CORRECT ANSWER!!! ,YOU WON {levels[i]}!!!\n")
               if i==4: #savepoints or checkpoints 
                    money='10,000 ₹'
               elif i==9:
                    money='3,20,000 ₹'
               elif i==15:
                    money='7,00,000,000 ₹'
          else:
               playsound.playsound(wrongans)
               print("WRONG ANSWER!!!")
               print("Your take home money is: ",money)
               break


              

