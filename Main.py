#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from sqlite3 import Cursor
import telebot
from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
import time
from datetime import datetime
import threading
import mysql.connector
from DDL import data

API_TOKEN = '7777678613:AAHVzcse6EpqUB5VKPTzesnfibw99yQQjZw'

bot = telebot.TeleBot(API_TOKEN)

user_steps = dict() 
user_data = dict() 
user_answers = dict() 

hide_keybored = ReplyKeyboardRemove()

config ={
    'user'      :   'root',
    'password'  :   'paswordn',
    'host'      :   'localhost',
    'database'  :   'tel_bot'
}

commands = {
    'start'             :   'start the bot',
    'help'              :   'show help menu',
    'profile'           :   'show user info',
    'Project'           :   'learn more',
}

def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)
bot.set_update_listener(listener)

@bot.message_handler(commands=['start'])
def commad_start_handler(message) :
    cid = message.chat.id
    user_first_name = message.chat.first_name 
    bot.send_message(cid , f'سلام {user_first_name}عزیز به ربات learn.code خوش آمدید.', reply_to_message_id= message.message_id)
    user_data[cid] = {'join_time': datetime.now()}
    show_language_menu(cid)

@bot.message_handler(commands=['help'])
def command_help_handler(message):
    cid = message.chat.id
    text = 'فهرست منو help  شما:\nشما در این ربات با انتخاب  یک نوع زبان برنامه نویسی و گرفتن هر روزی یک درس همراه با تمرین کد نویسی خودتون رو تقویت می کنید .\n'
    for command , desc in commands.items():
        text += f'/{command}: {desc}\n'
    bot.send_message(cid, text)

@bot.message_handler(commands=['profile'])
def command_profile_handler(message):
    cid = message.chat.id
   
    if cid not in user_data:
        bot.send_message(cid, "شما هنوز در ربات ثبت نام نکرده‌اید.")
        return

    user_info = user_data[cid]

    user_name = message.chat.first_name
    programming_language = user_info.get('زبان برنامه نویسی', 'نامشخص')
    level = user_info.get('سطح', 'نامشخص')
    

    user_score = sum(1 for u, c in zip(user_answers.get(cid, []), data["correct_answer"].get(programming_language, [])) if u == c)


    join_time = user_info.get('join_time')  
    if join_time:
        duration = datetime.now() - join_time
        duration_string = str(duration).split('.')[0]  
    else:
        duration_string = "نامشخص"

    profile_message = (
        f"📄 **پروفایل کاربر**\n"
        f"👤 **نام:** {user_name}\n"
        f"💻 **زبان برنامه‌نویسی:** {programming_language}\n"
        f"📊 **سطح:** {level}\n"
        f"🏆 **امتیاز:** {user_score}\n"
        f"⏳ **مدت زمان عضویت:** {duration_string}\n"
    )
    
    bot.send_message(cid, profile_message, parse_mode='Markdown')

def get_questions_from_db(language, level, cid):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT file_id, answer FROM `question` WHERE language = %s AND level_ques = %s", (language, level))
        questions = cursor.fetchall()
        return questions
    except mysql.connector.Error as err:
        bot.send_message(cid, f"خطای اتصال به پایگاه داده: {err}")
        return []
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


def insert_user_answer(cid, question_idx, answer):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `test` (user_id, question_id, user_answer, Date) VALUES (%s, %s, %s, %s)",
                       (cid, question_idx, answer, datetime.now()))
        conn.commit()
    except mysql.connector.Error as err:
        bot.send_message(cid, f"خطای درج پاسخ به پایگاه داده: {err}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()



def show_language_menu(cid):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Java','Python','C++')
    bot.send_message(cid,'زبان برنامه نویسی مورد علاقه خود را انتخاب کنید.', reply_markup= markup)
    user_steps[cid] = 'select_language'


@bot.message_handler(func=lambda message:user_steps.get(message.chat.id) == 'select_language')
def select_language(message):
    cid = message.chat.id
    language = message.text
    if language not in['Java' , 'Python', 'C++']:
        bot.send_message(cid , 'لطفا یکی از زبان هارو انتخاب کنید.')
        return
    user_data[cid] = {'زبان برنامه نویسی': language , 'سطح': '','پیشرفت':[] }
    bot.send_message(cid, f'شما زبان {language}را انتخاب کردید.')
    ask_for_level_test(cid)

def ask_for_level_test(cid):
    markup = ReplyKeyboardMarkup(resize_keyboard= True)
    markup.row('آماده ام', 'بازگشت')
    bot.send_message(cid,'برای امتحان تعیین سطح خود آماده هستید؟', reply_markup=markup)
    user_steps[cid] = 'level_test_request'

@bot.message_handler(func=lambda message: user_steps.get(message.chat.id) == 'level_test_request')
def level_test_request(message):
    cid = message.chat.id
    if message.text == 'آماده ام':
        start_level_test(cid)
    else:
        bot.send_message(cid , 'شما میتوانید انتخاب کنید که دوباره زبان خود را انتخاب کنید یا بقیه مراحل را از سر بگیرید.')
        show_language_menu(cid)

def start_level_test(cid):
    bot.send_message(cid, 'شروع امتحان سطح شما ...')
    user_answers[cid] = [] 
    user_data[cid]['current_question'] = 0  
    send_question(cid)

def send_question(cid):
    Cursor.execute("SELECT language, lesson_id, question_text, correct_answer FROM questions")
    questions = Cursor.fetchall()
    
    for question_idx, question in enumerate(questions):
        language, lesson_id, question_text, correct_answer = question
        
        question_file_id = lesson_id 

        options = [
            types.InlineKeyboardButton('A', callback_data=f'answer_{question_idx}_A'),
            types.InlineKeyboardButton('B', callback_data=f'answer_{question_idx}_B'),
            types.InlineKeyboardButton('C', callback_data=f'answer_{question_idx}_C'),
            types.InlineKeyboardButton('D', callback_data=f'answer_{question_idx}_D')
        ]
        markup = InlineKeyboardMarkup([options])
        
        bot.send_photo(cid, question_file_id, caption=question_text, reply_markup=markup)
        
        if cid not in user_data:
            user_data[cid] = {'current_question': 0}
        user_data[cid]['current_question'] += 1

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    data = call.data.split('_')
    question_idx = int(data[1])
    user_answer = data[2]

    Cursor.execute("SELECT correct_answer FROM questions")
    correct_answers = Cursor.fetchall()


    if user_answer == correct_answers[question_idx][0]:
        bot.send_message(call.from_user.id, 'پاسخ شما درست است!')
    else:
        bot.send_message(call.from_user.id, 'پاسخ شما نادرست است.')


@bot.callback_query_handler(func=lambda call: call.data.startswith('answer_'))
def handle_answer(call):
    cid = call.message.chat.id
    question_idx = int(call.data.split('_')[1]) 
    answer = call.data.split('_')[2]  
    user_answers[cid].append(answer)
    insert_user_answer(cid, question_idx, answer)

    send_question(cid)
    
def evaluate_level(cid):
    try:
        language = user_data[cid].get('زبان برنامه نویسی')
        if not language or language not in data["correct_answers"]:
            bot.send_message(cid, 'خطا در ارزیابی سطح: زبان برنامه‌نویسی نامعتبر.')
            return

        correct = data ["correct_answers"][language]
        user = user_answers.get(cid, [])
        score = sum(1 for u, c in zip(user, correct) if u == c)

        bot.send_message(cid, f'امتیاز شما: {score}/{len(correct)}')

        if score == len(correct):
            level = 'پیشرفته'
        elif score >= len(correct) // 2:
            level = 'متوسط'
        else:
            level = 'مبتدی'

        bot.send_message(cid, f'سطح شما: {level}')
        user_data[cid]['سطح'] = level
        ask_for_readiness(cid)

    except Exception as e:
        bot.send_message(cid, f'خطا در ارزیابی سطح: {e}')

def ask_for_readiness(cid,):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('آماده‌ام', 'نه، بعدا')
    bot.send_message(cid, 'ایا آماده دریافت درس امروز هستید؟',reply_markup=markup)
    user_steps[cid] = 'handle_next_readiness'

@bot.message_handler(func=lambda message: user_steps.get(message.chat.id) == 'handle_next_readiness')
def handle_next_readiness(message):
    cid = message.chat.id
    level = user_data[cid].get('سطح', 'مبتدی') 
    language = user_data[cid].get('زبان برنامه نویسی').lower()

    if message.text == 'آماده‌ام':

        if data["level_lessons"][language][level]:  
            send_first_lesson(cid, level, language)
        else:
            bot.send_message(cid, "درس‌هایی برای ارسال بیشتر وجود ندارد.")
        
    elif message.text == 'نه، بعدا':
        bot.send_message(cid, "باشه، هر زمان که آماده بودی بگو.")

def send_first_lesson(cid, level, language):
    if data["level_lessons"][language][level]: 
        lesson = data["level_lessons"][language][level].pop(0)
        bot.send_document(cid, f"درس شما: {lesson}")
        threading.Thread(target=wait_and_ask_next_lesson, args=(cid, level, language)).start()
    else:
        bot.send_message(cid, "پاسخی: درس جدیدی برای ارسال وجود ندارد.")

def wait_and_ask_next_lesson(cid, level, language):
    time.sleep(12 * 3600)  
    while data["level_lessons"][language][level]: 
        if cid not in user_data:
            break  
        ask_if_ready_for_next_lesson(cid)

def ask_if_ready_for_next_lesson(cid, language, level):
    if data["level_lessons"][language][level]: 
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('آماده‌ام', 'نه، بعدا')
        bot.send_message(cid, "درس قبلی رو خوندی؟ می‌خوای درس جدید رو بخونی؟", reply_markup=markup)
    else:
        bot.send_message(cid, "درس بیشتری برای ارسال وجود ندارد.")
 
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()