import codeforces as cf
import contest_time
import bot
def upcoming_contest_announcement(contest_id):
    upcoming_contest = cf.get_upcoming_contest()
    start_time_seconds=0
    duration_seconds = 0
    relative_time_seconds = 0
    name = ""
    for contest in upcoming_contest['result']:
        if contest['id'] == int(contest_id):
            name = contest['name']
            start_time_seconds = contest['startTimeSeconds']
            duration_seconds = contest['durationSeconds']
            relative_time_seconds = contest['relativeTimeSeconds']
            break

    remaining_time,need_announcment = contest_time.get_time(relative_time_seconds)
    if not need_announcment:
        return
    message = [
       '📢 Announcement: Upcoming Codeforces Contest! 🚀',
        f'Get ready, Coders ! {name} is just around the corner. Mark your calendars:',
        remaining_time
    ]
    bot.send_message(message)

def announce_contest_rank(messages):
    for msg in messages:
        bot.send_message(msg)
