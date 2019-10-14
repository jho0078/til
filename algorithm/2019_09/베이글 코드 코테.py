def getGameListWithState(gameInfoList):
    opened = []
    closed = []

    for game in gameInfoList:
        if game['state'] == 'CLOSED':
            closed.append(game)

        else:
            opened.append(game)

    gameInfoResult = sorted(opened, key=lambda game: game['rank'])

    gameInfoResult += closed

    return gameInfoResult


gameInfoList = [
    {
        'game_id': 1,
        'state': 'CLOSED',
        'rank': 1,
    },
    {
        'game_id': 3,
        'state': 'OPENED',
        'rank': 3,
    },
    {
        'game_id': 2,
        'state': 'OPENED',
        'rank': 2,
    }
]

print(getGameListWithState(gameInfoList))

#
# Your previous Plain Text content is preserved below:
#
# Club Vegas 는 유저들에게 플레이할 수 있는 게임들의 리스트를 제공합니다.
# 유저들은 게임 리스트 중 자신의 마음에 드는 게임을 선정하여 게임을 플레이할 수 있습니다.
# 베이글코드 서버팀에 근무하는 어피치는 게임 리스트의 순서를 잘 배치하는 코드를 짜려고 합니다.
# 게임 리스트에서의 순서와 상태를 결정하는 데에 고려사항은 다음과 같습니다.
#
# 1) 게임의 상태가 포함되지 않은, 게임 관련 정보가 담긴 object 의 리스트가 존재합니다. (예제 참고)
# 2) 게임에는 기본적으로 rank 정보가 있고, rank 가 낮은 순서가 게임 리스트 앞에 옵니다.
# 3) 게임의 상태는 OPENED, CLOSED 가 존재하고, 이는 유저별로 달라질 수 있습니다.
# 4) 유저의 클라이언트 버전이 낮으면, 플레이를 하지 못하는 게임이 있을 수 있습니다. 이 때 게임의 상태는 CLOSED 입니다.
# 5) 게임의 상태가 CLOSED 일 경우, 게임 리스트 맨 뒤로 보냅니다.
#
#
# 위 고려사항을 참고하여
#
# - 게임정보, 상태정보 등 필요한 데이터 구조를 알맞게 정의하고
# - 게임의 현재 상태정보를 포함한 게임 리스트를 리턴하는 함수
#
# 를 구현하세요. 사용 언어는 무관하고, 모든 필요한 데이터는 전역에 선언되어 있다고 가정해도 무방합니다.
#
# =============================================================
#
# const gameInfoList = [
#   {
#     game_id: 1,
#     ...
#     (other info like rank)
#   },
#   ...
# ];

# function getGameListWithState(...) {
#     ...
# }
#
# =============================================================
#
# Sample Output
# [
#     {
#         game_id: 1,
#         state: 'OPENED',
#         ...
#     },
#     {
#         game_id: 3,
#         state: 'OPENED',
#         ...
#     },
#     {
#         game_id: 2,
#         state: 'CLOSED',
#         ...
#     }
# ]
#
