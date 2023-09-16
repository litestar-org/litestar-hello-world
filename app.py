"""Minimal Litestar application."""
from __future__ import annotations

from asyncio import sleep
from typing import Any

from litestar import Litestar, get

__all__ = ("async_hello_world", "sync_hello_world")


@get("/async")
async def async_hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    await sleep(0.1)
    return {"hello": "world"}


@get("/sync", sync_to_thread=False)
def sync_hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    return {"hello": "world"}


app = Litestar(route_handlers=[sync_hello_world, async_hello_world])
