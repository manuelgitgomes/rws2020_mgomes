#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class Player():


    def __init__(self, player_name):
        self.player_name=player_name

        rospy.logwarn('I am ' + self.player_name)
        red_team = rospy.get_param('/red_team')
        green_team = rospy.get_param('/green_team')
        blue_team = rospy.get_param('/blue_team')
        print('Red Team =' + str(red_team))
        print('Green Team =' + str(green_team))
        print('Blue Team =' + str(blue_team))


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