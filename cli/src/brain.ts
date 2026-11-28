import type { Completion, Message, FunctionSpec } from "./types.js";
const BASE = (process.env.AEGIS_BASE_URL || "http://127.0.0.1:8000").replace(/\/$/, "");
export async function complete(messages: Message[], functions: FunctionSpec[]): Promise<Message> {
 const response = await fetch(`${BASE}/v1/chat/completions`, {method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify({model:"mr-aegis",messages,functions,function_call:"auto",temperature:0.2,top_p:0.8,max_length:1600,stream:false}),signal:AbortSignal.timeout(180000)});
 if(!response.ok) throw new Error(`Mr Aegis HTTP ${response.status}: ${(await response.text()).slice(0,1600)}`);
 const result = await response.json() as Completion; const message=result.choices?.[0]?.message;
 if(!message) throw new Error("Mr Aegis returned no assistant message."); return message;
}
export async function checkBrain(): Promise<void> { const r=await fetch(`${BASE}/v1/models`,{signal:AbortSignal.timeout(8000)}); if(!r.ok) throw new Error(`Mr Aegis health check failed: HTTP ${r.status}`); }
