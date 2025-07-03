from dotenv import load_dotenv
load_dotenv(override=True)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from browser_use.llm import ChatAzureOpenAI
from browser_use import Agent, Browser, BrowserConfig

app = FastAPI()
browser = Browser(config=BrowserConfig(headless=True))

current_agent = None

class QueryRequest(BaseModel):
    task: str

class QueryResponse(BaseModel):
    result: str

@app.post("/v1/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    global current_agent
    if not request.task:
        raise HTTPException(status_code=400, detail="Task cannot be empty")
    
    current_agent = Agent(
        task=request.task,
        llm=ChatAzureOpenAI(model="gpt-4.1"),
        browser=browser,
    )
    result = await current_agent.run()
    
    # return QueryResponse(result=result.all_results[-1].extracted_content)
    print(f"result >>>>>>> {result.final_result()}")
    return QueryResponse(result=result.final_result())

@app.get("/v1/terminate")
async def terminate():
    global current_agent
    if current_agent:
        if current_agent.browser_context:
            await current_agent.browser.close()
        return {"message": "Request terminated"}
    else:
        return {"message": "No active request to terminate"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5055)
