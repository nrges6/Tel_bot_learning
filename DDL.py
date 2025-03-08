import mysql.connector


config = {
    'user'      :    'root', 
    'password'  :    'paswordn', 
    'host'      :    'localhost', 
    'database'  :    'tel_bot'
}

data = {
    "question_images" :{
        'Python': ['AgACAgQAAxkBAAPaZ5PaXU8KF-5JLyfLSaTqL586lAoAAgzHMRvgQqBQlQgl-2aGpvEBAAMCAAN4AAM2BA', 
                   'AgACAgQAAxkBAAPcZ5PajyVupf09uXCNB2y4W6lPQyYAAg_HMRvgQqBQAQNBoiwtuSABAAMCAAN4AAM2BA',
                   'AgACAgQAAxkBAAIBsmeUqmquLNjZjlnqSVJ9W6AkcaJmAAIjxTEbp_6oULXJlU2DXPoCAQADAgADeQADNgQ',
                   'AgACAgQAAxkBAAPeZ5PapmnWhl1BhhXPl7weqV0JcI8AAhbHMRvgQqBQ3A_UNOpwNmYBAAMCAAN4AAM2BA',
                    'AgACAgQAAxkBAAPgZ5Papw2MAAEgAAG6oGOuHt4N02wXIQACF8cxG-BCoFByi6MHFtj5wwEAAwIAA3gAAzYE',
                   'AgACAgQAAxkBAAPiZ5PaqOjfxuBeWdTzclKifn9vBz8AAhjHMRvgQqBQhKWc23rdt6oBAAMCAAN4AAM2BA',
                   'AgACAgQAAxkBAAPjZ5PaqPWll7Mrya0xo8l-yqy0I2sAAhnHMRvgQqBQRyTJnxYSJ-8BAAMCAAN4AAM2BA',
                   'AgACAgQAAxkBAAPmZ5PaqGESaUpYJPhqX3PYAopVk2MAAhrHMRvgQqBQUpbS8wRze0cBAAMCAAN4AAM2BA',
                   'AgACAgQAAxkBAAPoZ5PaqZweLRhTlnPK5AHKBXBkwLsAAhvHMRvgQqBQmoORKeNr2zgBAAMCAAN4AAM2BA',
                   'AgACAgQAAxkBAAPpZ5Paqf6P3itlBhxq0pncD7Xia9gAAhzHMRvgQqBQvRO0Yl_oTKEBAAMCAAN4AAM2BA'
                   ],
   
        'Java': ['AgACAgQAAxkBAAP0Z5Pi6g3SDYKQydgevny0rFh8SOoAAqnEMRu93MBTbR_yJP_BwMUBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP1Z5Pi6qlRKMPg6hWvoKhnJIBkgbkAAqrEMRu93MBTdTT2uUCBPVkBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP2Z5Pi6johvv0y7XOK3Be5lKYh1uYAAqvEMRu93MBTupCxYI5kH3sBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP4Z5Pi6iz9F55vxMxh4mMysDO0uTkAAq3EMRu93MBTNVev9vOVKXcBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP3Z5Pi6jZp24un7AAB8bghl26Q6zuxAAKsxDEbvdzAU_trpPFCV6tSAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAP6Z5Pi6kL3a-r35DW0qwm6cJam8YMAAq_EMRu93MBT3FiSyQJnbd4BAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP7Z5Pi6sRC2oF_JeNV9q2IjKI_CDkAArDEMRu93MBTJuX7Z_OCOBQBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP5Z5Pi6mBfNlvxlPTlG1oPLp-EirwAAq7EMRu93MBT-AEzuZWervUBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP8Z5Pi6nJ3GmsKxbcEGELRm_rtF8wAArHEMRu93MBT630f32zvWiwBAAMCAAN5AAM2BA',
                'AgACAgQAAxkBAAP9Z5Pi6i_ie8AbNYKEqv3dSTSLTx4AArLEMRu93MBTdcu5YlK0NEEBAAMCAAN5AAM2BA'
        ],  

        'C++': ['AgACAgQAAxkBAAIBAAFnk-Q4vrqzlL1Fk3uJbJp36nsksQACO8cxG-BCoFDI-XsoOQ6uYAEAAwIAA3kAAzYE',
                'AgACAgQAAxkBAAIBAAFnk-Q4vrqzlL1Fk3uJbJp36nsksQACO8cxG-BCoFDI-XsoOQ6uYAEAAwIAA3kAAzYE',
                'AgACAgQAAxkBAAIBAmeT5DhZZZ45hxCiG9GUnkqOGr25AAI8xzEb4EKgUKKOQMfwV1zOAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAIBBGeT5DgjK2t7G5zuJNchlQKXGkmFAAI9xzEb4EKgUD_kEGXLn5mNAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAIBBWeT5DiA48C9icEOL5t4smLA4wiCAAJexDEb0F9YU-i4XxilDFjuAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAIBBmeT5DjT8qeY_wABgQLZsxixOpJO4QACPscxG-BCoFBBYuZd00YaxAEAAwIAA3kAAzYE',
                'AgACAgQAAxkBAAIBA2eT5DhWAQABtgtjM8ty9cqX3tA8tQACYcQxG9BfWFO1yvbo5yulOQEAAwIAA3kAAzYE',
                'AgACAgQAAxkBAAIBB2eT5DhoDHwELjPP-GVrAnYr8nxiAAJdxDEb0F9YU_Ts9EuckVZvAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAIBCWeT5DinbFXVZamlaefNsndhWM58AAJaxDEb0F9YU7P-1zF2nY1WAQADAgADeQADNgQ',
                'AgACAgQAAxkBAAIBCGeT5DiW8pOhvXqYWwk2eu37VlRjAAI_xzEb4EKgUIVgPW_ZTVQMAQADAgADeQADNgQ',
        ]
    },
    "correct_answers" : {
        'Python': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'A', 'B'],
        'Java': ['B', 'C', 'C', 'B', 'B', 'B', 'C', 'A', 'C', 'C'],
        'C++': ['A', 'C', 'A', 'B', 'A', 'B', 'C', 'B', 'A', 'D'],
    },
    "level_lessons" : {
        'python':{
            'مبتدی' :[' BQACAgQAAxkBAAICwWeZOgZZmV72nAtzsFMcgkE277vCAAK6GAACMl7JUGGq1LTMmmpoNgQ',
                        ' BQACAgQAAxkBAAIDB2eac5_1NuSS8jTUsixQFlPajp6DAAJhGAACQYnZUKq1j8XYwdO5NgQ',
                        ' BQACAgQAAxkBAAIDCWeac6htioSAgpwRX5Ly-13z3paGAAJiGAACQYnZUAm3mrp9T7igNgQ',
                        ' BQACAgQAAxkBAAIDC2eac7KhK9uFKC9TFVCBkTEQpCWDAAJjGAACQYnZUGk0eDg5SenTNgQ',
                        ' BQACAgQAAxkBAAIDDWeac76S_OyrgnSIyraHbSEyBiYRAAJkGAACQYnZUNlXJw3t642SNgQ',
                        ' BQACAgQAAxkBAAIDD2eac8cbE2Ah6UOU6bxSOVxDf-8FAAJlGAACQYnZUKMXvjJoNozjNgQ',
                        ' BQACAgQAAxkBAAIDEWeac9Acpl4nYa9qca2AKfFx3dIhAAJmGAACQYnZUAlg7Zt8ETMRNgQ',
                        ' BQACAgQAAxkBAAIDE2eac9jbJ-xhy1PI1pgaoQypAAE0FwACZxgAAkGJ2VCikBEV8F4JNjYE',
                        ' BQACAgQAAxkBAAIDFWeac-DGgyzh3M1_urIriju2ODtiAAJoGAACQYnZUCjVCnybqOafNgQ',
                        ' BQACAgQAAxkBAAIDF2eac-kY9fJzWAvMfd3fQdidQMhMAAJpGAACQYnZUGjztH0BvYIdNgQ',
                        ' BQACAgQAAxkBAAIDGWeac--8gj0-INDuc4gZH2sNozKWAAJqGAACQYnZUDDWfyMqO5GENgQ',
                        ' BQACAgQAAxkBAAIDG2eac_cf-jGyvC1un6V5RPjUKHogAAJrGAACQYnZUFDwWd2ggh6ZNgQ',
                        ' BQACAgQAAxkBAAIDHWeadA3R5V-4LedBqn5vswez7sobAAJsGAACQYnZUPtc1cZ0_rHbNgQ',
                        ' BQACAgQAAxkBAAIDH2eadA4uuMUVKHMOKa8IuZTJ6y01AAJtGAACQYnZUKF-fxM2mta-NgQ',
                        ' BQACAgQAAxkBAAIDIWeadBAn6YI53iLXncET0j2KM2juAAJuGAACQYnZUBtk5YPikXEZNgQ',
                        ' BQACAgQAAxkBAAIDI2eadC5_T2tmmAhF-GtIgK4OEBN7AAJvGAACQYnZUMOkXzdphLuoNgQ',
                        ' BQACAgQAAxkBAAIDJWeadDA0w0mr0kchTIu-PZOoBzsvAAJwGAACQYnZUOwBt25QclkLNgQ',
                        ' BQACAgQAAxkBAAIDJ2eadDMH4Mz69mYvbn11Jby43Rr2AAJxGAACQYnZUMoKn87o79sfNgQ',
                        ' BQACAgQAAxkBAAIDKWeadDWlEowYmBTsigon7tnwJMF9AAJyGAACQYnZUKeOxOiQ0pJDNgQ',
                        ' BQACAgQAAxkBAAIDK2eadDjSDA75ucEljkCyemv9iyHlAAJzGAACQYnZUKV-zKGNQPMHNgQ',
                        ' BQACAgQAAxkBAAIDLWeadDnteibmMA5OkyY8q40M0LAZAAJ0GAACQYnZUBIu6qa4hX9uNgQ',
                        ' BQACAgQAAxkBAAIDL2eadDvoBj7n9723MTN_Q9nmkzrJAAJ1GAACQYnZUATibCF0h0ikNgQ',
                        ' BQACAgQAAxkBAAIDMWeadD0xZ-GKOSXDsim0JULhnVJcAAJ2GAACQYnZUI3Xr2OnZkc7NgQ',
                        ' BQACAgQAAxkBAAIDM2eadEFB4nNmteIk1XEKq2SbJxETAAJ3GAACQYnZUD7T1lytLa14NgQ',
                        ' BQACAgQAAxkBAAIDNWeadET3bnfm_mWNP9B4CZmReywkAAJ4GAACQYnZUCTQs1DL9JMaNgQ',
                        ' BQACAgQAAxkBAAIDN2eadEXEut_gi9ovn73EsdM-JDLiAAJ5GAACQYnZUBozlg5YSDNgNgQ'],
            'متوسط' : [],
            'پیشرفته' : [],    
        },
        'java' : {
            'مبتدی':[],
            'متوسط':[],
            'پیشرفته':[]
        },
        'C++' : {
            'مبتدی':[],
            'متوسط' : [],
            'پیشرفته' : []
        }
    }
}   

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    print ("connected to MYSQL server successfully")

    insert_question_query = """
    INSERT INTO questions (language, lesson_id, question_text, correct_answer )
    VALUES (%s, %s, %s, %s)
    """
    for language, images in data["question_images"].items():
        correct_answers_list = data["correct_answers"].get(language, [])
        for i, file_id in enumerate(images):
            question_text = f"Question {i + 1} for {language}"  
            answer = correct_answers_list[i] if i < len(correct_answers_list) else None
            cursor.execute(insert_question_query, (language, file_id, question_text, answer))

    connection.commit()
    print("Questions inserted successfully!")

    create_lessons_table = """
    CREATE TABLE IF NOT EXISTS lessons (
        language VARCHAR(50) NOT NULL,
        level VARCHAR(20) NOT NULL,
        document_id VARCHAR (100) NoT NULL,
        PRIMARY KEY (language, level, document_id)
    )
    """
    cursor.execute(create_lessons_table)
    print("Table 'lessons' created succrssfully!")

    insert_lesson_query = """
    INSERT  IGNORE INTO lessons (language, level, document_id)
    VALUES (%s, %s, %s)
    """

    for language, levels in data["level_lessons"].items():
        for level, document_ids in levels.items():
           for document_id in document_ids:
            cursor.execute(insert_lesson_query, (language, level, document_id))

    connection.commit()
    print("Lessons inserted successfully!")

    cursor.execute("create database if not exists tel_bot")
    print("database 'tel_bot' created successfuly")

    cursor.execute("Use tel_bot")

    create_questions_table = """
    CREATE TABLE IF NOT EXISTS questions (
        question_id INT AUTO_INCREMENT PRIMARY KEY,
        language VARCHAR(50),
        lesson_id VARCHAR(100),
        question_text TEXT,
        correct_answer VARCHAR(50)
    )
    """
    cursor.execute(create_questions_table)
    print("Table 'questions' created successfully!")

    
    create_user_table = """
    CREATE TABLE IF NOT EXISTS user (
        user_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        level INT NOT NULL,
        language VARCHAR(10) NOT NULL,
        score INT
    )
    """
    cursor.execute(create_user_table)
    print("Table 'user' created successfully!")

  
    create_test_table = """
    CREATE TABLE IF NOT EXISTS test (
        test_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id INT UNSIGNED NOT NULL,
        question_id INT,
        user_answer TEXT,
        Date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """
    cursor.execute(create_test_table)
    print("Table 'test' created successfully!")

   
    create_study_materials_table = """
    CREATE TABLE IF NOT EXISTS study_materials (
        materialId INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        title TEXT NOT NULL,
        level INT NOT NULL,
        price FLOAT(10, 2),
        description TEXT,
        file_id VARCHAR(100) NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_study_materials_table)
    print("Table 'study_materials' created successfully!")

   
    create_sale_table = """
    CREATE TABLE IF NOT EXISTS sale (
        date DATETIME DEFAULT CURRENT_TIMESTAMP,
        user_id INT UNSIGNED NOT NULL,
        sale_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """
    cursor.execute(create_sale_table)
    print("Table 'sale' created successfully!")

   
    create_sale_row_table = """
    CREATE TABLE IF NOT EXISTS sale_row (
        sale_id INT UNSIGNED NOT NULL,
        material_id INT UNSIGNED NOT NULL,
        PRIMARY KEY (sale_id, material_id),
        FOREIGN KEY (material_id) REFERENCES study_materials(materialId)
    )
    """
    cursor.execute(create_sale_row_table)
    print("Table 'sale_row' created successfully!")

    
    create_result_table = """
    CREATE TABLE IF NOT EXISTS result (
        result_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id INT UNSIGNED NOT NULL,
        language VARCHAR(10),
        level INT UNSIGNED NOT NULL,
        score INT NOT NULL,
        status VARCHAR(50),
        feedback TEXT,
        FOREIGN KEY (user_id) REFERENCES user(user_id)
    )
    """
    cursor.execute(create_result_table)
    print("Table 'result' created successfully!")

    
    insert_question = """
    INSERT INTO questions (language, lesson_id, question_text, correct_answer)
    VALUES (%s, %s, %s, %s)
    """
    question_data = ('Python', 'lesson_1', 'What is Python?', 'A')
    cursor.execute(insert_question, question_data)
    connection.commit()
    print("Question inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        cursor.close()
       # connection.close()
        #print("Connection to MySQL closed.")
