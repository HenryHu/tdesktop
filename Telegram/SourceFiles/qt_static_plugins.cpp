/*
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
*/
#include <QtCore/QtPlugin>

#ifdef Q_OS_WIN
Q_IMPORT_PLUGIN(QWebpPlugin)
Q_IMPORT_PLUGIN(QWindowsIntegrationPlugin)
#elif defined Q_OS_MAC // Q_OS_WIN
Q_IMPORT_PLUGIN(QWebpPlugin)
Q_IMPORT_PLUGIN(QCocoaIntegrationPlugin)
Q_IMPORT_PLUGIN(QGenericEnginePlugin)
#elif defined Q_OS_LINUX || defined Q_OS_FREEBSD // Q_OS_WIN | Q_OS_MAC
#endif // Q_OS_WIN | Q_OS_MAC | Q_OS_LINUX | Q_OS_FREEBSD
