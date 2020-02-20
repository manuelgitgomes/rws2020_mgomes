#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class Player():


    def __init__(self, player_name):
        self.player_name=player_name

        red_team = rospy.get_param('/red_team')
        green_team = rospy.get_param('/green_team')
        blue_team = rospy.get_param('/blue_team')
        print('Red Team = ' + str(red_team))
        print('Green Team = ' + str(green_team))
        print('Blue Team = ' + str(blue_team))

        if self.player_name in red_team:
            self.my_team, self.prey_team, self.hunter_team = 'red', 'green', 'blue'
            self.my_players, self.prey_players, self.hunter_players = red_team, green_team, blue_team
        elif self.player_name in green_team:
            self.my_team, self.prey_team, self.hunter_team = 'green', 'blue', 'red'
            self.my_players, self.prey_players, self.hunter_players = green_team, blue_team, red_team
        elif self.player_name in blue_team:
            self.my_team, self.prey_team, self.hunter_team = 'blue', 'red', 'green'
            self.my_players, self.prey_players, self.hunter_players = blue_team, red_team, green_team
        else:
            rospy.logerr('My name is not in any team. I want to play!')
            exit(0)

        rospy.logwarn('I am ' + self.player_name + ' and team ' + self.my_team + ' is the greatest. Team ' + self.prey_team + ' are all going to die! Be careful with ' + self.hunter_team + ' team.')




def callback(msg):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print("Recieved a message containing string " + msg.data)

def main():
    print("Hello player node!")
    rospy.init_node('mgomes', anonymous=False)

    player = Player('mgomes')
    rospy.Subscriber("chatter", String, callback)
    rospy.spin()

if __name__ == "__main__":
    main()