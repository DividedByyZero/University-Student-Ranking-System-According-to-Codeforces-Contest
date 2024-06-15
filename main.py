import time
import googlesheet_api_init as sheetapi
from current_rank_list import *
from sheet_column_indexing import *
import codeforces as cf
import elo_rating as elo
import contest
import announcement as give_announcement
import ranklist_announcement as ranking

 
def main():
    contest_id = contest.get_contest_id()
    is_updated = False
    if contest_id==0:
        is_updated=True
        print("Already Updated !")
    if contest.announce_contest_id != -1:
        give_announcement.upcoming_contest_announcement(contest.announce_contest_id)
    
    if is_updated : 
        return
    usernames = cf.get_codeforces_id()
    current_rating_list = cf.get_current_rating_list()
    print(current_rating_list)
    contest_info = cf.get_contest_info(contest_id)

    rank_list = cf.fetch_api(usernames, contest_id)
    sorted_rank_list = sorted(rank_list, key=lambda x: x[1], reverse=False)
    count = 1

    for name, rank in sorted_rank_list: 
        if name in current_rating_list:
            elo.add_coder(name, count, current_rating_list[name])
            count += 1

    elo.calculate_new_rating()
    for coder in elo.coders:  
        name = coder['name']
        new_rating = coder['post_rating']
        rating_change = coder['rating_change']
        cell_index = cf.find(name)
        total_contest_participation = sheetapi.records[cell_index - 2]['Number of Participated Contest']
        sheetapi.targetSheet.update_cell(cell_index, indexing['Ratings'], new_rating)
        sheetapi.targetSheet.update_cell(cell_index, indexing['Number of Participated Contest'], int(total_contest_participation) + 1)
        sheetapi.targetSheet.update_cell(cell_index, indexing['Last Rating Change'], rating_change)
        time.sleep(3)

    time.sleep(10)
    sheetapi.targetSheet.sort((indexing['Ratings'], 'des'))
    time.sleep(15)
    rank_message = ranking.make_rank(contest_info['result']['contest']['name'],contest_info['result']['contest']['id'],sorted_rank_list)
    give_announcement.announce_contest_rank(rank_message)
    cf.update_total_contest()

if __name__ == "__main__":
    main()