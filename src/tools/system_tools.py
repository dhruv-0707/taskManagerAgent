from langchain.tools import tool
from pydantic import BaseModel, Field
import platform
import datetime

# --- Validation Schemas ---
class CalculateInput(BaseModel):
    operation: str = Field(..., description="The operation to perform: 'add', 'subtract', 'multiply', 'divide'")
    x: float = Field(..., description="The first number")
    y: float = Field(..., description="The second number")

class FileWriteInput(BaseModel):
    filename: str = Field(..., description="The name of the file to write to. Must be safe text.")
    content: str = Field(..., description="The content to write into the file.")

# --- Tool Implementations with Error Handling ---

@tool("safe_calculator", args_schema=CalculateInput)
def safe_calculator(operation: str, x: float, y: float) -> str:
    """
    Performs basic arithmetic operations safely. 
    Useful for precise calculations validation.
    """
    try:
        if operation == "add":
            return str(x + y)
        elif operation == "subtract":
            return str(x - y)
        elif operation == "multiply":
            return str(x * y)
        elif operation == "divide":
            if y == 0:
                return "Error: Division by zero is not allowed."
            return str(x / y)
        else:
            return f"Error: Unknown operation '{operation}'"
    except Exception as e:
        return f"Error executing calculation: {str(e)}"

@tool("get_system_time")
def get_system_time() -> str:
    """Returns the current system time and date."""
    return datetime.datetime.now().isoformat()

@tool("get_os_info")
def get_os_info() -> str:
    """Returns information about the operating system."""
    return f"{platform.system()} {platform.release()}"
