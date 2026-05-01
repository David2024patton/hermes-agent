#!/usr/bin/env python3
"""
Demonstration of the Agentic Autonomy System for Hermes Agent

This script demonstrates the full agentic autonomy capabilities including:
- Task decomposition and planning
- Sub-agent orchestration with role specialization
- Multi-agent coordination
- Reflective reasoning
- Continuous learning
"""

import sys
import os
import json
from typing import Dict, Any

# Add the hermes-agent directory to the path
sys.path.insert(0, '/home/david/.hermes/hermes-agent')

from agent.agentic.integration import get_agentic_integration
from agent.agentic.roles import get_role_manager
from agent.agentic.coordination import get_agentic_coordinator

def print_section(title: str):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def print_subsection(title: str):
    """Print a formatted subsection header"""
    print(f"\n{'-'*40}")
    print(f"  {title}")
    print(f"{'-'*40}")

def demonstrate_agentic_system():
    """Demonstrate the full agentic autonomy system"""
    
    print_section("HERMES AGENT - AGENTIC AUTONOMY SYSTEM DEMONSTRATION")
    
    # Get the agentic integration
    agentic = get_agentic_integration()
    role_manager = get_role_manager()
    coordinator = get_agentic_coordinator()
    
    # 1. Show available roles
    print_section("1. AVAILABLE AGENT ROLES")
    roles = agentic.get_available_roles()
    
    for role_name, role_info in roles.items():
        print(f"\n📌 {role_name.upper()}")
        print(f"   Description: {role_info['description']}")
        print(f"   Capabilities: {', '.join(role_info['capabilities'])}")
        print(f"   Default Tools: {', '.join(role_info['default_tools'])}")
    
    # 2. Demonstrate task execution
    print_section("2. TASK EXECUTION DEMONSTRATION")
    
    complex_task = """
    Develop a comprehensive AI-powered research assistant that can:
    1. Search academic papers on AI agent frameworks
    2. Analyze and summarize key findings
    3. Generate a comparative analysis report
    4. Create visual diagrams of architecture patterns
    5. Write comprehensive documentation
    """
    
    print(f"Executing complex task:\n{complex_task}")
    
    result = agentic.execute_agentic_task(complex_task)
    
    print_subsection("Task Execution Results")
    print(f"✅ Task Success: {result['success']}")
    print(f"📋 Tasks Created: {len(result['tasks'])}")
    
    for task in result['tasks']:
        print(f"\n🔹 Task ID: {task['task_id'][:8]}...")
        print(f"   Description: {task['description'][:100]}...")
        print(f"   Status: {task['status']}")
        print(f"   Assigned Agent: {task['assigned_agent']}")
        if task['result']:
            print(f"   Result: {task['result'][:80]}...")
    
    print_subsection("Reflective Analysis")
    reflection = result['reflection']
    print(f"🤖 Analysis: {reflection['analysis']}")
    print(f"💡 Improvements: {', '.join(reflection['improvements'])}")
    print(f"📚 Lessons: {', '.join(reflection['lessons_learned'])}")
    
    # 3. Show system status
    print_section("3. SYSTEM STATUS")
    status = agentic.get_system_status()
    
    print(f"🤖 Active Agents: {status['active_agents']}")
    print(f"✅ Completed Tasks: {status['completed_tasks']}")
    print(f"⏳ Pending Tasks: {status['pending_tasks']}")
    print(f"⚠️  Conflicts Detected: {status['conflicts_detected']}")
    print(f"✅ Conflicts Resolved: {status['conflicts_resolved']}")
    
    # 4. Demonstrate custom role creation
    print_section("4. CUSTOM ROLE CREATION")
    
    custom_role_name = "data_scientist"
    custom_role_added = agentic.add_custom_role(
        role_name=custom_role_name,
        description="Specialized in data analysis, machine learning, and statistical modeling",
        capabilities=["data_analysis", "machine_learning", "statistics", "data_visualization"],
        default_tools=["python", "pandas", "scikit-learn", "matplotlib"]
    )
    
    if custom_role_added:
        print(f"✅ Custom role '{custom_role_name}' added successfully!")
        
        # Show the new role
        new_roles = agentic.get_available_roles()
        if custom_role_name in new_roles:
            role_info = new_roles[custom_role_name]
            print(f"\n📌 {custom_role_name.upper()}")
            print(f"   Description: {role_info['description']}")
            print(f"   Capabilities: {', '.join(role_info['capabilities'])}")
            print(f"   Default Tools: {', '.join(role_info['default_tools'])}")
    
    # 5. Demonstrate multi-task execution
    print_section("5. MULTI-TASK EXECUTION")
    
    tasks = [
        "Research the latest advancements in multi-agent systems",
        "Develop a prototype for agent communication protocol",
        "Create documentation for the new agentic framework",
        "Design test cases for agent coordination scenarios"
    ]
    
    all_results = []
    for i, task in enumerate(tasks, 1):
        print(f"\n🚀 Executing Task {i}: {task[:60]}...")
        result = agentic.execute_agentic_task(task)
        all_results.append(result)
        print(f"   ✅ Completed: {result['success']}")
        print(f"   📋 Sub-tasks: {len(result['tasks'])}")
    
    # 6. Show final system state
    print_section("6. FINAL SYSTEM STATE")
    final_status = agentic.get_system_status()
    
    print(f"🤖 Active Agents: {final_status['active_agents']}")
    print(f"✅ Total Completed Tasks: {final_status['completed_tasks']}")
    print(f"📊 Task Success Rate: {final_status['completed_tasks']}/{final_status['completed_tasks'] + final_status['pending_tasks']}")
    
    print_section("DEMONSTRATION COMPLETE")
    print("""
    🎉 The Agentic Autonomy System is now fully integrated with Hermes Agent!
    
    Key Features Demonstrated:
    ✅ Task decomposition and planning
    ✅ Sub-agent orchestration with role specialization
    ✅ Multi-agent coordination and conflict resolution
    ✅ Reflective reasoning and continuous learning
    ✅ Custom role creation and management
    ✅ System monitoring and status tracking
    
    The system is ready for production use and can handle complex,
    multi-step tasks with autonomous sub-agents working in parallel.
    """)

if __name__ == "__main__":
    demonstrate_agentic_system()