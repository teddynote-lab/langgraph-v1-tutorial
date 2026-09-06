# LangGraph V1 튜토리얼

LangGraph V1의 핵심 개념과 실전 활용 방법을 다루는 한국어 Jupyter Notebook 튜토리얼 모음입니다. 초보자부터 중급 개발자까지 LangGraph를 활용한 AI 에이전트 개발 방법을 단계별로 학습할 수 있습니다.

모든 실습은 [LangChain 공식 문서](https://docs.langchain.com/) (`https://docs.langchain.com/llms.txt`) 의 최신 패턴을 기준으로 작성되었습니다.

## 목차

1. [환경 설정](#환경-설정)
2. [사용 라이브러리 버전](#사용-라이브러리-버전)
3. [튜토리얼 목록](#튜토리얼-목록)
4. [시작하기](#시작하기)
5. [참고 자료](#참고-자료)

## 환경 설정

### 1. UV 설치

UV는 빠르고 효율적인 Python 패키지 관리자입니다.

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. 의존성 설치

`pyproject.toml` / `uv.lock` 에 고정된 버전을 그대로 설치합니다. (가상 환경은 `.venv` 에 자동 생성됩니다.)

```bash
uv sync
```

가상 환경을 직접 활성화하려면:

```bash
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

### 3. 환경 변수 설정

`.env.example` 파일을 `.env`로 복사하고 API 키를 설정합니다:

```bash
cp .env.example .env
```

`.env` 파일 내용:
```
OPENAI_API_KEY=
ANTHROPIC_API_KEY=

LANGSMITH_API_KEY=
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=LangGraph-Tutorial

TAVILY_API_KEY=
```

### 4. 기본 모델

실습 코드는 기본적으로 OpenAI `gpt-5.4` 를 사용합니다 (`init_chat_model("gpt-5.4")`). 다른 모델을 사용하려면 `gpt-5.4-mini`, `anthropic:claude-sonnet-5` 등으로 바꿔 실행할 수 있습니다. (Ollama 로컬 모델 예제는 `PART02/Ch02/03-QuickStart-LangGraph-Ollama.ipynb` 를 참고하세요.)

## 사용 라이브러리 버전

| 패키지 | 버전 | 비고 |
|:---|:---|:---|
| `langchain` | >= 1.4.0 | `create_agent`, 미들웨어, `langchain.mcp` (MCP 내장 지원) |
| `langchain-core` | >= 1.6 | 표준 `reasoning_effort` 파라미터, 표준 모델 예외 타입 |
| `langgraph` | >= 1.2.11 | 이벤트 스트리밍 v3, 노드 단위 오류 핸들러/타임아웃 |
| `langgraph-checkpoint-postgres` / `-redis` | >= 3.1 / >= 0.5 | 영속 체크포인터 |
| `langchain-anthropic` / `langchain-openai` | >= 1.7 / >= 1.6 | 모델 통합 |
| `fastmcp` / `mcp` | >= 4.0 / >= 2.1 | MCP 서버 작성 (FastMCP 4) 및 MCP Python SDK 2.x |
| `deepagents` | >= 0.7 | Deep Agents |
| `langchain-teddynote` | >= 0.5.4 | 그래프 시각화, 스트리밍 헬퍼 등 |

> **MCP 안내**: LangChain 1.4부터 MCP 클라이언트가 `langchain.mcp` (`MCPAdapter`) 로 내장되어 기존 `langchain-mcp-adapters` (`MultiServerMCPClient`) 를 대체합니다. MCP Python SDK 2.x 에서는 `mcp.server.fastmcp` 경로가 제거되었으므로 서버는 `from fastmcp import FastMCP` 를 사용합니다. 자세한 내용은 [마이그레이션 가이드](https://docs.langchain.com/oss/python/migrate/langchain-mcp-adapters)를 참고하세요.

## 튜토리얼 목록

### PART 01. LangGraph 기초

**Ch01. 그래프 생성하기**

| 노트북 | 내용 |
|:---|:---|
| `01-LangGraph-Introduction.ipynb` | LangGraph 소개, 기본 개념 |
| `01-LangGraph-Models.ipynb` | `init_chat_model`, 모델 파라미터, `reasoning_effort`, 토큰 사용량, 멀티모달 |
| `01-QuickStart-LangGraph-Tutorial.ipynb` | 챗봇 → 도구 → 메모리 → HITL → 타임트래블 퀵스타트 |
| `02-LangGraph-Messages.ipynb` | 메시지 타입과 컨텐츠 블록 |
| `02-QuickStart-LangGraph-Graph-API.ipynb` | Graph API 퀵스타트 |
| `03-LangGraph-Building-Graphs.ipynb` | StateGraph, 노드/엣지, 조건부 분기, `Command`/`Send` |

### PART 02. 에이전트

| 챕터 | 노트북 | 내용 |
|:---|:---|:---|
| Ch02. 에이전트 | `01-LangGraph-Agents.ipynb` | `create_agent`, 도구, 미들웨어, 재시도/폴백 |
| | `02-LangGraph-ChatBot.ipynb` | 대화형 챗봇 구축 |
| | `02-LangGraph-Tools.ipynb` | `@tool`, `ToolRuntime`, 도구 오류 처리 |
| | `03-QuickStart-LangGraph-Ollama.ipynb` | Ollama 로컬 모델로 에이전트 실행 |
| Ch03. Runtime | `04-LangGraph-Runtime.ipynb` | `Runtime` 객체, `context_schema`, Store, Stream writer |
| Ch04. 구조화된 출력 | `05-LangGraph-Structured-Output.ipynb` | `response_format`, `ToolStrategy`, `ProviderStrategy` |
| Ch05. Human-in-the-Loop | `02-LangGraph-Human-In-The-Loop.ipynb`, `06-LangGraph-Human-In-the-Loop.ipynb` | `interrupt`, `HumanInTheLoopMiddleware`, `Command(resume=...)` |

### PART 03. 에이전트 확장

| 챕터 | 노트북 | 내용 |
|:---|:---|:---|
| Ch06. 미들웨어 | `01-LangGraph-Middleware.ipynb` | `before_model`, `after_model`, `wrap_model_call`, `dynamic_prompt`, 내장 미들웨어 |
| Ch07. 컨텍스트 엔지니어링 | `03-LangGraph-Context-Engineering.ipynb` | Model / Tool / Life-cycle 컨텍스트 |
| Ch08. 가드레일 | `04-LangGraph-Guardrail.ipynb` | `PIIMiddleware`, 커스텀 가드레일 |
| Ch09. 메모리 추가하기 | `01-LangGraph-Add-Memory.ipynb` | `InMemorySaver`, `thread_id`, 단기 메모리 |
| | `02-LangGraph-Memory-Postgres.ipynb` | `PostgresSaver`, `PostgresStore` |
| | `04-LangGraph-Agent-With-Memory.ipynb` | 장기 메모리 (Store) 와 에이전트 |
| | `09-LangGraph-DeleteMessages.ipynb` | `RemoveMessage` 로 메시지 삭제 |
| | `12-LangGraph-Add-Conversation-Summary.ipynb` | 대화 요약 (`SummarizationMiddleware`) |
| Ch10. MCP 실습 | `01-LangGraph-MCP-Tutorial.ipynb` | `langchain.mcp` `MCPAdapter`, FastMCP 서버, stdio / Streamable HTTP, 다중 서버 |

### PART 04. 멀티에이전트

| 챕터 | 노트북 | 내용 |
|:---|:---|:---|
| Ch11. Supervisor | `01-LangGraph-Supervisor.ipynb`, `03-LangGraph-Multi-Agent-Supervisor.ipynb` | Supervisor 패턴, 서브에이전트 |
| Ch12. 협업 네트워크 | `02-LangGraph-Multi-Agent-Collaboration.ipynb` | 에이전트 간 핸드오프 |
| Ch13. 계층적 에이전트 팀 | `04-LangGraph-Hierarchial-Agent-Team.ipynb` | 계층적 팀 구성 |

### PART 05. 핵심 기능 구현하기

| 챕터 | 노트북 | 내용 |
|:---|:---|:---|
| Ch14. Agent 구축 | `03-LangGraph-Agent.ipynb` | LangGraph 로 직접 에이전트 루프 구현 |
| Ch15. 상태 수동 업데이트 | `07-LangGraph-Manual-State-Update.ipynb` | `update_state`, 중간 단계 개입 |
| Ch16. 상태 커스터마이징 | `08-LangGraph-State-Customization.ipynb` | 커스텀 상태 스키마 |
| Ch17. ToolNode | `10-LangGraph-ToolNode.ipynb` | `ToolNode`, `tools_condition` |
| Ch18. 병렬 노드 실행 | `11-LangGraph-Branching.ipynb` | 분기와 팬아웃/팬인 |
| Ch19. 서브그래프 | `13-LangGraph-Subgraph.ipynb` | 서브그래프 추가 및 사용 |
| Ch20. 서브그래프 입출력 변환 | `14-LangGraph-Subgraph-Transform-State.ipynb` | 상태 변환 |
| Ch21. 스트리밍 모드 | `03-LangGraph-Streaming.ipynb`, `05-LangGraph-Streaming-Outputs.ipynb`, `15-LangGraph-Streaming-Steps.ipynb` | `stream_mode`, 토큰 스트리밍, `astream_events` v2 / 이벤트 스트리밍 v3 |
| Ch22. Agent Chat UI | `Agent-Chat-UI-OSS.ipynb` | `langgraph dev` + Agent Chat UI 배포 |

### Appendix

| 폴더 | 내용 |
|:---|:---|
| `A-RAG응용/` | Naive RAG → Groundedness Check → Web Search → Query Rewrite → Agentic / Corrective / Self / Adaptive RAG |
| `B-Use-Cases/` | Agent Simulation, Prompt Generation, Plan-and-Execute, SQL Agent, Research Assistant |
| `C-GraphRAG/` | Neo4j Text2Cypher (GraphRAG) |

## 시작하기

### 1. 저장소 클론

```bash
git clone https://github.com/braincrew-lab/langgraph-v1-tutorial.git
cd langgraph-v1-tutorial
```

### 2. 환경 설정

위의 [환경 설정](#환경-설정) 섹션을 따라 UV를 설치하고 `uv sync` 로 의존성을 설치합니다.

### 3. Jupyter 실행

```bash
uv run jupyter lab
```

또는 VS Code의 Jupyter 확장을 사용할 수 있습니다. (커널로 `.venv` 를 선택하세요.)

### 4. 권장 학습 순서

PART 01 → PART 02 → PART 03 → PART 04 → PART 05 → Appendix 순서로 진행하는 것을 권장합니다.

## 필수 요구사항

- **Python**: 3.11 이상 (`.python-version` 참고)
- **API Keys**:
  - OpenAI API Key (기본 모델 `gpt-5.4`)
  - Anthropic API Key (Claude 모델 사용 시, 선택사항)
  - Tavily API Key (웹 검색 실습)
  - LangSmith API Key (추적, 선택사항)
- **기본 지식**:
  - Python 프로그래밍 기초
  - 비동기 프로그래밍 개념 (async/await)
  - LLM 및 프롬프트 엔지니어링 기초

## 프로젝트 구조

```
langgraph-v1-tutorial/
├── README.md
├── .env.example
├── pyproject.toml                 # 의존성 정의
├── uv.lock                        # 의존성 잠금 파일
├── assets/                        # 공용 이미지
├── data/                          # 실습 데이터
├── PART01-LangGraph-기초/
├── PART02-에이전트/
├── PART03-에이전트-확장/
│   └── Ch10-LangGraph-MCP-실습/server/   # FastMCP 서버 예제
├── PART04-멀티에이전트/
├── PART05-핵심-기능-구현하기/
└── Appendix/
```

## 참고 자료

### 공식 문서
- [LangChain / LangGraph Documentation](https://docs.langchain.com/)
- [LangGraph (Python) 가이드](https://docs.langchain.com/oss/python/langgraph/overview)
- [LangChain (Python) 가이드](https://docs.langchain.com/oss/python/langchain/overview)
- [LangChain Python API Reference](https://reference.langchain.com/python/)
- [FastMCP Documentation](https://gofastmcp.com/)

### 관련 리소스
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [UV Documentation](https://docs.astral.sh/uv/)

### 커뮤니티
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangGraph GitHub](https://github.com/langchain-ai/langgraph)
- [LangChain Discord](https://discord.gg/langchain)

## 라이선스

이 튜토리얼은 교육 목적으로 제공됩니다.

## 기여하기

튜토리얼 개선 사항이나 오류를 발견하신 경우 Issue를 생성하거나 Pull Request를 제출해 주세요.

---

**Happy Learning with LangGraph V1!**
