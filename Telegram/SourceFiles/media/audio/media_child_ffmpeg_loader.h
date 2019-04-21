/*
This file is part of Telegram Desktop,
the official desktop application for the Telegram messaging service.

For license and copyright information please follow this link:
https://github.com/telegramdesktop/tdesktop/blob/master/LEGAL
*/
#pragma once

#include "media/audio/media_audio_ffmpeg_loader.h"
#include "media/streaming/media_streaming_utility.h"

namespace Media {

struct ExternalSoundData {
	Streaming::CodecPointer codec;
	Streaming::FramePointer frame;
	int32 frequency = Media::Player::kDefaultFrequency;
	int64 length = 0;
	float64 speed = 1.; // 0.5 <= speed <= 2.
};

struct ExternalSoundPart {
	AudioMsgId audio;
	Streaming::Packet packet;
};

class ChildFFMpegLoader : public AbstractAudioFFMpegLoader {
public:
	ChildFFMpegLoader(std::unique_ptr<ExternalSoundData> &&data);

	bool open(crl::time positionMs) override;

	bool check(const FileLocation &file, const QByteArray &data) override {
		return true;
	}

	ReadResult readMore(QByteArray &result, int64 &samplesAdded) override;
	void enqueuePackets(std::deque<Streaming::Packet> &&packets) override;
	void setForceToBuffer(bool force) override;
	bool forceToBuffer() const override;

	bool eofReached() const {
		return _eofReached;
	}

	~ChildFFMpegLoader();

private:
	// Streaming player reads first frame by itself and provides it together
	// with the codec context. So we first read data from this frame and
	// only after that we try to read next packets.
	ReadResult readFromInitialFrame(
		QByteArray &result,
		int64 &samplesAdded);

	std::unique_ptr<ExternalSoundData> _parentData;
	std::deque<Streaming::Packet> _queue;
	bool _forceToBuffer = false;
	bool _eofReached = false;

};

} // namespace Media
