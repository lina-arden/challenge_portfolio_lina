from pages.base_page import BasePage


class ADD_A_MATCH_FORM(BasePage):
    table = //*[@id="__next"]/div[1]/main/div[2]
    title_form = //*[@id="__next"]/div[1]/main/div[2]/form/div[1]
    fields_to_fill = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]
    my_team_field = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]
    enemy_name_team_field = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]
    my_team_score_field = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]
    enemy_team_score = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]
    date_field = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[5]
    match_location = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[6]
    rating_field = //*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[13]