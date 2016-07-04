import fresh_tomatoes
import media
import shows

#Create the instances of movie class
independence_day = media.Media("Independence Day: Resurgence",
                                "http://t1.gstatic.com/images?q=tbn:ANd9GcSGT7ibrynE3qOCfdU9N4tcyuKoVHE7CR_Xrgse14AbDECJpYFA",
                                "https://www.youtube.com/watch?v=RfJgT89hEME")

finding_dory =  media.Media("Finding Dory",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcTPxyoxzLf33_chM3uqooaT3tiyEBbQmqJb0Ndbvpt6qfQ4ybIk",
                            "https://www.youtube.com/watch?v=MKJA-VLpiCo")

me_before_you = media.Media("Me Before You",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcR-Pi0mGMztx_eCHb3f7BrSiL0Gy_YfMk0Ef6WUSPx2KZ135n-a",
                            "https://www.youtube.com/watch?v=Eh993__rOxA")

#Create the instances of show class
Game_Thrones = shows.TV_Show("Game of Thrones",
                            "http://www.gstatic.com/tv/thumb/tvbanners/12502846/p12502846_b_v8_aa.jpg",
                            "https://www.youtube.com/watch?v=KWZGAExj-es",
                            "[1,2,3]")

#put them in a list
media_list = [independence_day, finding_dory, me_before_you, Game_Thrones]

#use the fresh_tomatoes file to display and run the movies in the webbrowser
fresh_tomatoes.open_movies_page(media_list)
