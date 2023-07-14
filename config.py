token = '988685350:AAHrdWAe2KUKe_PM9TbwqW4FvNrwatTMRi8'
usrs = []
animals = ['dog', 'cat', 'mouse', 'rabbit', 'fox', 'bear', 'panda', 'white_bear', 'koala', 'tiger', 'cow', 'lion',
           'pig', 'frog', 'monkey', 'cock', 'penguin', 'chick', 'duck', 'eagle',
           'owl', 'bat', 'wolf', 'hog', 'horse', 'unicorn', 'bee', 'caterpillar', 'butterfly',
           'snail', 'ladybug', 'ant', 'fly', 'bug', 'grasshopper', 'spider', 'scorpion',
           'turtle', 'snake', 'lizard', 'T-rex', 'diplodog', 'octopus', 'shrimp', 'lobster',
           'crab', 'puffer_fish', 'dolphin', 'whale', 'shark', 'seal', 'crocodile', 'leopard', 'zebra',
           'gorilla', 'mammoth', 'elephant', 'hippopotamus', 'rhinoceros', 'camel', 'giraffe', 'kangaroo', 'bull',
           'ram', 'lama', 'goat', 'dear', 'turkey', 'peacock', 'parrot', 'swan', 'flamingo', 'raccoon',
           'skunk', 'beaver', 'sloth', 'squirrel', 'hedgehog', 'dragon']
for i in range(0, 79):
    animals[i] = "img/"+animals[i]

emoji = ['🐕', '🐈', '🐁', '🐇', '🦊', '🐻', '🐼', '🐻‍❄️', '🐨', '🐅', '🐄', '🦁',
           '🐖', '🐸', '🐒', '🐓', '🐧', '🐥', '🦆', '🦅',
           '🦉', '🦇', '🐺', '🐗', '🐎', '🦄', '🐝', '🐛', '🦋',
           '🐌', '🐞', '🐜', '🪰', '🪲', '🦗', '🕷', '🦂',
           '🐢', '🐍', '🦎', '🦖', '🦕', '🐙', '🦐', '🦞',
           '🦀', '🐡', '🐬', '🐳', '🦈', '🦭', '🐊', '🐆', '🦓',
           '🦍', '🦣', '🐘', '🦛', '🦏', '🐪', '🦒', '🦘', '🐃',
           '🐑', '🦙', '🐐', '🦌', '🦃', '🦚', '🦜', '🦢', '🦩', '🦝',
           '🦨', '🦫', '🦥', '🐿', '🦔', '🐲']


def check(i):
    for i in range(0, 79):
        print(animals[i], ' - ', i, emoji[i])
    # for i in range(0, 79):
    #     print(emoji[i], '-', i)


# check(0)
