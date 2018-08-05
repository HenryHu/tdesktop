/*
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
*/
#pragma once

namespace Platform {
namespace Audio {

void Init();

void DeInit();

} // namespace Audio
} // namespace Platform

// Platform dependent implementations.

#if defined Q_OS_MAC || defined Q_OS_LINUX || defined Q_OS_FREEBSD
namespace Platform {
namespace Audio {

inline void Init() {
}

inline void DeInit() {
}

} // namespace Audio
} // namespace Platform
#elif defined Q_OS_WINRT || defined Q_OS_WIN // Q_OS_MAC || Q_OS_LINUX || Q_OS_FREEBSD
#include "platform/win/audio_win.h"
#endif // Q_OS_MAC || Q_OS_LINUX || Q_OS_WINRT || Q_OS_WIN || Q_OS_FREEBSD
