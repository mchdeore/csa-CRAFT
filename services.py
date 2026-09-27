"""Wire protocol interfaces to concrete implementations."""

from auth import DictAuth
from chat import DeepSeekChat
from protocols import AuthProvider, ChatProvider, WorkspaceStore
from storage import JsonFileStore

auth_provider: AuthProvider = DictAuth()
store: WorkspaceStore = JsonFileStore()
chat_provider: ChatProvider = DeepSeekChat()
