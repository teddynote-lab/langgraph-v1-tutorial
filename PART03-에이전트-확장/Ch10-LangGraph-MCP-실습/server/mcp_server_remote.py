from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from fastmcp import FastMCP

# FastMCP 서버 초기화 및 구성
mcp = FastMCP(
    "Current Time",  # MCP 서버 이름
    instructions="주어진 시간대의 현재 시간 정보를 제공합니다",
)


@mcp.tool
async def get_current_time(timezone: str = "Asia/Seoul") -> str:
    """지정된 시간대의 현재 시간 정보를 가져옵니다.

    이 함수는 요청된 시간대의 현재 시스템 시간을 반환합니다.

    Args:
        timezone: 현재 시간을 조회할 시간대(IANA 이름). 기본값은 "Asia/Seoul"입니다.

    Returns:
        지정된 시간대의 현재 시간 정보가 포함된 문자열
    """
    try:
        # 지정된 시간대의 현재 시간을 가져옵니다 (표준 라이브러리 zoneinfo 사용)
        current_time = datetime.now(ZoneInfo(timezone))

        # 시간을 문자열로 포맷합니다
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")

        return f"Current time in {timezone} is: {formatted_time}"
    except ZoneInfoNotFoundError:
        return f"Error: Unknown timezone '{timezone}'. Please provide a valid IANA timezone."
    except Exception as e:
        return f"Error getting time: {str(e)}"


if __name__ == "__main__":
    # 서버가 시작됨을 알리는 메시지를 출력합니다
    print("MCP Remote 서버가 실행 중입니다... (http://127.0.0.1:8002/mcp)")

    # Streamable HTTP 전송 방식으로 서버를 시작합니다 (포트 8002)
    # FastMCP 4.x 에서는 transport="http" 가 Streamable HTTP 를 의미합니다
    mcp.run(transport="http", host="127.0.0.1", port=8002)
