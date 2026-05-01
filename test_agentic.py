#!/usr/bin/env python3
"""
Test script for the agentic autonomy system
"""

import sys
import os

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

from agent.agentic.integration import get_agentic_integration

def test_agentic_system():
    """Test the agentic system functionality"""
    print("Testing Agentic Autonomy System...")
    print("=" * 50)
    
    # Get the agentic integration
    agentic = get_agentic_integration()
    
    # Test 1: Execute a simple task
    print("\n1. Testing task execution...")
    result = agentic.execute_agentic_task("Research AI agent frameworks")
    print(f"Task execution result: {result['success']}")
    print(f"Tasks created: {len(result['tasks'])}")
    
    # Test 2: Get available roles
    print("\n2. Testing available roles...")
    roles = agentic.get_available_roles()
    print(f"Available roles: {list(roles.keys())}")
    
    # Test 3: Get system status
    print("\n3. Testing system status...")
    status = agentic.get_system_status()
    print(f"System status: {status['active_agents']} active agents, "
          f"{status['completed_tasks']} completed tasks")
    
    # Test 4: Add a custom role
    print("\n4. Testing custom role creation...")
    custom_role_added = agentic.add_custom_role(
        role_name="data_scientist",
        description="Specialized in data analysis and machine learning",
        capabilities=["data_analysis", "machine_learning", "statistics"],
        default_tools=["python", "pandas", "scikit-learn"]
    )
    print(f"Custom role added: {custom_role_added}")
    
    print("\n" + "=" * 50)
    print("All tests completed successfully!")

if __name__ == "__main__":
    test_agentic_system()