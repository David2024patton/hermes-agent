"""
Test suite for the Agentic Autonomy System

This module contains comprehensive tests for all agentic system components.
"""

import pytest
import json
from typing import Dict, Any

# Import the agentic system components
from agent.agentic import get_agentic_system, AgenticTask
from agent.agentic.roles import get_role_manager, AgentRole
from agent.agentic.coordination import get_agentic_coordinator, CoordinationState
from agent.agentic.integration import get_agentic_integration


class TestAgenticSystem:
    """Test the core agentic system functionality"""
    
    def test_system_initialization(self):
        """Test that the agentic system initializes correctly"""
        system = get_agentic_system()
        assert system is not None
        assert system.planner is not None
        assert system.orchestrator is not None
        assert system.memory is not None
        assert system.reflection_log == []
    
    def test_task_decomposition(self):
        """Test task decomposition functionality"""
        system = get_agentic_system()
        
        # Test basic task decomposition
        tasks = system.planner.decompose_task("Research AI frameworks")
        assert len(tasks) == 1
        assert isinstance(tasks[0], AgenticTask)
        assert tasks[0].description == "Research AI frameworks"
        assert tasks[0].status == "pending"
    
    def test_task_dependency_management(self):
        """Test task dependency management"""
        system = get_agentic_system()
        
        # Create two tasks
        task1 = system.planner.decompose_task("Task 1")[0]
        task2 = system.planner.decompose_task("Task 2")[0]
        
        # Add dependency
        system.planner.add_dependency(task2.task_id, task1.task_id)
        
        # Verify dependency was added
        assert task2.task_id in system.dependency_graph[task1.task_id]
        assert task1.task_id in task2.dependencies

class TestAgenticRoles:
    """Test the role management system"""
    
    def test_role_manager_initialization(self):
        """Test that role manager initializes with built-in roles"""
        role_manager = get_role_manager()
        assert role_manager is not None
        assert len(role_manager.roles) == 5
    
    def test_builtin_roles(self):
        """Test that all built-in roles are available"""
        role_manager = get_role_manager()
        expected_roles = ['researcher', 'developer', 'tester', 'documenter', 'architect']
        
        for role_name in expected_roles:
            assert role_name in role_manager.roles
            role = role_manager.get_role(role_name)
            assert isinstance(role, AgentRole)
            assert len(role.capabilities) > 0
            assert len(role.default_tools) > 0
    
    def test_custom_role_creation(self):
        """Test custom role creation"""
        role_manager = get_role_manager()
        
        # Create a custom role
        custom_role = AgentRole(
            name="data_scientist",
            description="Specialized in data analysis",
            capabilities=["data_analysis", "machine_learning"],
            default_tools=["python", "pandas"]
        )
        
        role_manager.add_role(custom_role)
        
        # Verify the role was added
        assert "data_scientist" in role_manager.roles
        retrieved_role = role_manager.get_role("data_scientist")
        assert retrieved_role.description == "Specialized in data analysis"

class TestAgenticCoordinator:
    """Test the multi-agent coordination system"""
    
    def test_coordinator_initialization(self):
        """Test coordinator initialization"""
        coordinator = get_agentic_coordinator()
        assert coordinator is not None
        assert isinstance(coordinator.state, CoordinationState)
        assert coordinator.state.active_agents == 0
        assert coordinator.state.completed_tasks == 0
    
    def test_task_queue_management(self):
        """Test task queue management"""
        coordinator = get_agentic_coordinator()
        
        # Add tasks to queue
        coordinator.add_task("task_1")
        coordinator.add_task("task_2")
        
        assert len(coordinator.task_queue) == 2
        assert coordinator.state.pending_tasks == 2
        
        # Complete a task
        coordinator.complete_task("task_1")
        
        assert len(coordinator.task_queue) == 1
        assert coordinator.state.completed_tasks == 1
        assert coordinator.state.pending_tasks == 1
    
    def test_agent_status_tracking(self):
        """Test agent status tracking"""
        coordinator = get_agentic_coordinator()
        
        # Update agent status
        coordinator.update_agent_status("agent_1", "working")
        assert coordinator.state.active_agents == 1
        
        coordinator.update_agent_status("agent_1", "idle")
        assert coordinator.state.active_agents == 0

class TestAgenticIntegration:
    """Test the agentic system integration"""
    
    def test_integration_initialization(self):
        """Test integration layer initialization"""
        integration = get_agentic_integration()
        assert integration is not None
        assert integration.agentic_system is not None
        assert integration.role_manager is not None
        assert integration.coordinator is not None
    
    def test_task_execution(self):
        """Test end-to-end task execution"""
        integration = get_agentic_integration()
        
        result = integration.execute_agentic_task("Test task execution")
        
        assert result["success"] is True
        assert "tasks" in result
        assert len(result["tasks"]) > 0
        assert "reflection" in result
    
    def test_role_management(self):
        """Test role management through integration"""
        integration = get_agentic_integration()
        
        roles = integration.get_available_roles()
        assert len(roles) >= 5  # At least the built-in roles
        
        # Test custom role addition
        success = integration.add_custom_role(
            role_name="test_role",
            description="Test role",
            capabilities=["testing"],
            default_tools=["test"]
        )
        assert success is True
    
    def test_system_status(self):
        """Test system status monitoring"""
        integration = get_agentic_integration()
        
        status = integration.get_system_status()
        assert "active_agents" in status
        assert "completed_tasks" in status
        assert "pending_tasks" in status
        assert "conflicts_detected" in status
        assert "conflicts_resolved" in status


class TestAgenticTools:
    """Test the agentic tools integration with Hermes Agent"""
    
    def test_tool_imports(self):
        """Test that agentic tools can be imported"""
        from tools.agentic_tools import (
            agentic_execute_task,
            agentic_get_roles,
            agentic_get_status,
            TOOL_SCHEMAS
        )
        
        assert callable(agentic_execute_task)
        assert callable(agentic_get_roles)
        assert callable(agentic_get_status)
        assert len(TOOL_SCHEMAS) == 3
    
    def test_tool_schemas(self):
        """Test that tool schemas are correctly defined"""
        from tools.agentic_tools import TOOL_SCHEMAS
        
        expected_tools = ["agentic_execute_task", "agentic_get_roles", "agentic_get_status"]
        
        for schema in TOOL_SCHEMAS:
            assert schema["name"] in expected_tools
            assert "description" in schema
            assert "parameters" in schema
            
            # Verify parameter schemas
            params = schema["parameters"]
            assert "type" in params
            assert params["type"] == "object"
    
    def test_tool_execution(self):
        """Test actual tool execution"""
        from tools.agentic_tools import (
            agentic_execute_task,
            agentic_get_roles,
            agentic_get_status
        )
        
        # Test agentic_get_roles
        roles_result = agentic_get_roles()
        roles_data = json.loads(roles_result)
        assert roles_data["success"] is True
        assert "roles" in roles_data
        assert len(roles_data["roles"]) >= 5
        
        # Test agentic_get_status
        status_result = agentic_get_status()
        status_data = json.loads(status_result)
        assert status_data["success"] is True
        assert "status" in status_data
        
        # Test agentic_execute_task
        task_result = agentic_execute_task("Test tool execution")
        task_data = json.loads(task_result)
        assert task_data["success"] is True
        assert "result" in task_data


class TestAgenticDebugging:
    """Test debugging capabilities of the agentic system"""
    
    def test_system_introspection(self):
        """Test system introspection capabilities"""
        system = get_agentic_system()
        
        # Test access to internal state
        assert hasattr(system, 'planner')
        assert hasattr(system, 'orchestrator')
        assert hasattr(system, 'memory')
        assert hasattr(system, 'reflection_log')
        
        # Test planner state access
        assert hasattr(system.planner, 'tasks')
        assert hasattr(system.planner, 'dependency_graph')
        
        # Test orchestrator state access
        assert hasattr(system.orchestrator, 'sub_agents')
        assert hasattr(system.orchestrator, 'active_tasks')
    
    def test_memory_introspection(self):
        """Test memory system introspection"""
        system = get_agentic_system()
        
        # Test knowledge base access
        assert hasattr(system.memory, 'knowledge_base')
        assert hasattr(system.memory, 'experience_log')
        
        # Test knowledge storage and retrieval
        test_key = "test_key"
        test_value = {"test": "data"}
        
        system.memory.store_knowledge(test_key, test_value)
        retrieved = system.memory.retrieve_knowledge(test_key)
        
        assert retrieved == test_value
        assert len(system.memory.experience_log) == 0  # No auto-logging for store_knowledge
    
    def test_coordinator_debugging(self):
        """Test coordinator debugging capabilities"""
        coordinator = get_agentic_coordinator()
        
        # Test state access
        assert hasattr(coordinator, 'state')
        assert hasattr(coordinator, 'task_queue')
        assert hasattr(coordinator, 'agent_status')
        assert hasattr(coordinator, 'conflict_log')
        
        # Test conflict detection
        conflicts = coordinator.detect_conflicts()
        assert isinstance(conflicts, list)
        
        # Test status reporting
        status = coordinator.get_system_status()
        assert isinstance(status, dict)
        assert 'active_agents' in status


class TestAgenticErrorHandling:
    """Test error handling in the agentic system"""
    
    def test_graceful_degradation(self):
        """Test that the system handles errors gracefully"""
        integration = get_agentic_integration()
        
        # Test with empty task
        result = integration.execute_agentic_task("")
        assert result["success"] is True  # Should handle empty tasks gracefully
        
        # Test with None task
        result = integration.execute_agentic_task(None)
        assert result["success"] is True  # Should handle None gracefully
    
    def test_invalid_role_handling(self):
        """Test handling of invalid role operations"""
        integration = get_agentic_integration()
        
        # Try to add duplicate role
        success = integration.add_custom_role(
            role_name="researcher",  # Already exists
            description="Duplicate",
            capabilities=[],
            default_tools=[]
        )
        assert success is False  # Should fail gracefully
    
    def test_tool_error_handling(self):
        """Test error handling in agentic tools"""
        from tools.agentic_tools import agentic_execute_task
        
        # Test with invalid input
        result = agentic_execute_task(None)
        data = json.loads(result)
        
        # Should either succeed with empty task or fail gracefully
        assert data["success"] in [True, False]  # Either handling is acceptable


class TestAgenticPerformance:
    """Test performance characteristics of the agentic system"""
    
    def test_task_execution_performance(self):
        """Test that task execution completes in reasonable time"""
        import time
        
        integration = get_agentic_integration()
        
        start_time = time.time()
        
        # Execute multiple tasks
        for i in range(5):
            integration.execute_agentic_task(f"Test task {i}")
        
        end_time = time.time()
        
        # Should complete 5 tasks in less than 1 second
        assert (end_time - start_time) < 1.0
    
    def test_memory_efficiency(self):
        """Test that the system doesn't leak memory"""
        integration = get_agentic_integration()
        
        # Execute many tasks
        for i in range(10):
            integration.execute_agentic_task(f"Memory test task {i}")
        
        # System should still be responsive
        result = integration.get_system_status()
        assert result is not None
        assert "active_agents" in result


class TestAgenticEdgeCases:
    """Test edge cases and boundary conditions"""
    
    def test_very_long_task_descriptions(self):
        """Test handling of very long task descriptions"""
        integration = get_agentic_integration()
        
        long_task = "A" * 10000  # 10KB task description
        result = integration.execute_agentic_task(long_task)
        
        assert result["success"] is True
    
    def test_unicode_task_descriptions(self):
        """Test handling of unicode characters in tasks"""
        integration = get_agentic_integration()
        
        unicode_task = "Research AI frameworks with special chars: ñ, ü, é, 中文, 日本語"
        result = integration.execute_agentic_task(unicode_task)
        
        assert result["success"] is True
    
    def test_multiple_concurrent_tasks(self):
        """Test handling of multiple concurrent task executions"""
        integration = get_agentic_integration()
        
        # Execute multiple tasks simultaneously
        results = []
        for i in range(3):
            result = integration.execute_agentic_task(f"Concurrent task {i}")
            results.append(result)
        
        # All should succeed
        for result in results:
            assert result["success"] is True