from instapy import InstaPy
from instapy.util import smart_run

# login credentials
insta_username = 'coder_2x'
insta_password = '0D19IE'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    max_followers=4590,
                                    min_followers=45,
                                    min_following=77)

    session.set_dont_include(["friend1", "friend2", "friend3"])
    session.set_dont_like(["pizza", "#store"])

    # actions
    session.like_by_tags(["coding","java","python","programming"], amount=5)
    # Follow user based on hashtags (without liking the image)

    session.follow_by_tags(['coding', 'programming'], amount=5)
    # default enabled=False, ~ every 4th image will be commented on

    session.set_do_comment(enabled=True, percentage=25)
    session.set_comments(['Awesome', 'Really Cool', 'I like your stuff'])
    # Interact with specific users' tagged posts
# set_do_like, set_do_comment, set_do_follow are applicable

    session.set_do_follow(enabled=False, percentage=50)
    session.set_comments(["Cool", "Super!"])
    session.set_do_comment(enabled=True, percentage=80)
    session.set_do_like(True, percentage=70)
    session.interact_by_users_tagged_posts(['user1', 'user2', 'user3'], amount=5, randomize=True, media='Photo')
