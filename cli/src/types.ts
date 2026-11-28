export type Mode = "Ask" | "Plan" | "Build" | "Debug" | "Agent";
export type Role = "system" | "user" | "assistant" | "function";
export interface Message { role: Role; content: string | null; function_call?: { name: string; arguments: string }; }
export interface FunctionSpec { name: string; description: string; parameters: Record<string, unknown>; }
export interface Completion { choices?: Array<{ message?: Message; finish_reason?: string }>; }
