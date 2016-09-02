import argparse
import twitter

parser = argparse.ArgumentParser(description='Dit is Opdracht 7, IFSCP 1516')
parser.add_argument('-u', action="store", help="Username of twitter user", required=True)

class opdracht7():
    args = parser.parse_args()
    consumer_key = 'V4rpRc6p1OzOqMNeimcLIhOk5'
    consumer_secret = 'IEh7Bj40KGh0mvKwnZNhYoYDwWUZrqlCK9q7Csw8wGoTUqAIvn'
    access_token = '771481584788799488-MYkDTt5Is9NfSAnbjottOnVkqFdomYv'
    access_secret = 'tXfaUXFaUR45LaEyVXGiNsQWCJzyfWPmqJCLrNHLSBmKV'
    user = ''

    def __init__(self):
        self.args = parser.parse_args()
        # self.consumer_key = self.args.consk
        # self.consumer_secret = self.args.conss
        # self.access_token = self.args.accesst
        # self.access_secret = self.args.accesss
        self.user = self.args.u

        api = twitter.Api(consumer_key=self.consumer_key,
                          consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token,
                          access_token_secret=self.access_secret)
        api.VerifyCredentials()
        friends = api.GetFollowers(screen_name=self.user)
        for friend in friends:
            try:
                print(friend.name + " - " + friend.screen_name)
            except SyntaxError:
                continue


if __name__ == "__main__":
    opdracht7()