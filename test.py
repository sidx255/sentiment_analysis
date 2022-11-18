import tweepy
import tensorflow as tf
print(tf.__version__)


print(tf.config.list_physical_devices('GPU'))
print(tf.test.is_built_with_cuda())

# CONSUMER_KEY = ''
# CONSUMER_SECRET = ''
# ACCESS_TOKEN = ''
# ACCESS_TOKEN_SECRET = ''

# auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth,wait_on_rate_limit=True)

# status = "Testing!"
# api.update_status(status=status)