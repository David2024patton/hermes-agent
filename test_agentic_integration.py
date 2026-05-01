#!/usr/bin/env python3
"""
Test the agentic tools integration with Hermes Agent
"""

import sys
import os

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

# Import the tools registry
from tools.registry import registry
from tools.agentic_tools import register_agentic_tools

def test_agentic_tools_integration():
    """Test that agentic tools are properly registered"""
    print("Testing Agentic Tools Integration...")
    print("=" * 50)
    
    # Register the agentic tools
    register_agentic_tools(registry)
    
    # Test 1: Check if tools are registered
    print("\n1. Testing tool registration...")
    agentic_tools = ["agentic_execute_task", "agentic_get_roles", "agentic_get_status"]
    
    for tool_name in agentic_tools:
        if registry.has_tool(tool_name):
            print(f"✓ {tool_name} registered successfully")
        else:
            print(f"✗ {tool_name} NOT registered")
            return False
    
    # Test 2: Test tool execution
    print("\n2. Testing tool execution...")
    
    # Test agentic_get_roles
    try:
        roles_result = registry.call_tool("agentic_get_roles", {})
        print("✓ agentic_get_roles executed successfully")
        print(f"  Roles found: {len(roles_result['roles'])}")
    except Exception as e:
        print(f"✗ agentic_get_roles failed: {e}")
        return False
    
    # Test agentic_get_status
    try:
        status_result = registry.call_tool("agentic_get_status", {})
        print("✓ agentic_get_status executed successfully")
        print(f"  Active agents: {status_result['status']['active_agents']}")
    except Exception as e:
        print(f"✗ agentic_get_status failed: {e}")
        return False
    
    # Test agentic_execute_task
    try:
        task_result = registry.call_tool("agentic_execute_task", {
            "task_description": "Test agentic task execution"
        })
        print("✓ agentic_execute_task executed successfully")
        print(f"  Task success: {task_result['success']}")
    except Exception as e:
        print(f"✗ agentic_execute_task failed: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("All agentic tools integration tests passed!")
    return True

if __name__ == "__main__":
    success = test_agentic_tools_integration()
    sys.exit(0 if success else 1)