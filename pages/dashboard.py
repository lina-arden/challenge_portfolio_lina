from pages.base_page import BasePage


class Dashboard(BasePage):
    button_home_xpath = //*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span
    button_players_xpath = //*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span
    button_language_xpath = //*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span
    button_sign_out_xpath = //*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span
    statistics_grid_xpath = //*[@id="__next"]/div[1]/main/div[2]
    players_count_container = //*[@id="__next"]/div[1]/main/div[2]/div[1]
    matches_count_container = //*[@id="__next"]/div[1]/main/div[2]/div[2]
    reports_count_container = //*[@id="__next"]/div[1]/main/div[2]/div[3]
    events_count_container = //*[@id="__next"]/div[1]/main/div[2]/div[4]
    main_container = //*[@id="__next"]/div[1]/main/div[3]
