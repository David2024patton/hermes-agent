"""
Agentic Tool for Hermes Agent

This tool integrates the agentic autonomy system with Hermes Agent's tool system.
"""

import json
from typing import Dict, Any
from agent.agentic.integration import get_agentic_integration

def check_agentic_requirements() -> bool:
    """Check if agentic system is available"""
    try:
        get_agentic_integration()
        return True
    except Exception:
        return False

def agentic_execute_task(task_description: str, role_hint: str = "auto") -> str:
    """
    Execute a task using the agentic autonomy system
    
    Args:
        task_description: The task to execute
        role_hint: Optional role hint (researcher, developer, etc.)
    
    Returns:
        JSON string with execution results
    """
    try:
        agentic = get_agentic_integration()
        
        # Execute the task
        result = agentic.execute_agentic_task(task_description)
        
        return json.dumps({
            "success": True,
            "message": "Agentic task executed successfully",
            "result": result
        })
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        })

def agentic_get_roles() -> str:
    """
    Get available agentic roles
    
    Returns:
        JSON string with role information
    """
    try:
        agentic = get_agentic_integration()
        roles = agentic.get_available_roles()
        
        return json.dumps({
            "success": True,
            "roles": roles
        })
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        })

def agentic_get_status() -> str:
    """
    Get current agentic system status
    
    Returns:
        JSON string with system status
    """
    try:
        agentic = get_agentic_integration()
        status = agentic.get_system_status()
        
        return json.dumps({
            "success": True,
            "status": status
        })
    except Exception as e:
        return json.dumps({
            "success": False,
            "error": str(e)
        })

# Tool registration for Hermes Agent
TOOL_SCHEMAS = [
    {
        "name": "agentic_execute_task",
        "description": "Execute a task using the agentic autonomy system with specialized sub-agents",
        "parameters": {
            "type": "object",
            "properties": {
                "task_description": {
                    "type": "string",
                    "description": "The task to execute using the agentic system"
                },
                "role_hint": {
                    "type": "string",
                    "description": "Optional role hint for task assignment (researcher, developer, tester, etc.)",
                    "default": "auto"
                }
            },
            "required": ["task_description"]
        }
    },
    {
        "name": "agentic_get_roles",
        "description": "Get information about available agentic roles and their capabilities",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    },
    {
        "name": "agentic_get_status",
        "description": "Get current status of the agentic autonomy system",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
]

def register_agentic_tools(registry):
    """Register agentic tools with the Hermes Agent tool registry"""
    registry.register(
        name="agentic_execute_task",
        toolset="agentic",
        schema=TOOL_SCHEMAS[0],
        handler=lambda args, **kw: agentic_execute_task(
            task_description=args.get("task_description", ""),
            role_hint=args.get("role_hint", "auto")
        ),
        check_fn=check_agentic_requirements,
        requires_env=[]
    )
    
    registry.register(
        name="agentic_get_roles",
        toolset="agentic",
        schema=TOOL_SCHEMAS[1],
        handler=lambda args, **kw: agentic_get_roles(),
        check_fn=check_agentic_requirements,
        requires_env=[]
    )
    
    registry.register(
        name="agentic_get_status",
        toolset="agentic",
        schema=TOOL_SCHEMAS[2],
        handler=lambda args, **kw: agentic_get_status(),
        check_fn=check_agentic_requirements,
        requires_env=[]
    )