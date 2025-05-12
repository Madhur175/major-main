from app import mysql

class AudioSentiment:
    def add_sentiment(self, audio_file_name, sentiment):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO audio_sentiments (audio_file_name, sentiment) VALUES (%s, %s)", (audio_file_name, sentiment))
        mysql.connection.commit()
        cur.close()

    def get_sentiments(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM audio_sentiments")
        data = cur.fetchall()
        cur.close()
        return data
