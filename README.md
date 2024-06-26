# pyannote.audio

## Error

It seems like version error in numpy and pyannote.audio.

```shell
$ python main.py

  File "/Users/mio256/pyannote_audio/main.py", line 13, in <module>
    diarization = pipeline(input("Enter the path to the wav file: "), num_speakers=int(input("Enter the number of speakers: ")))
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mio256/pyannote_audio/venv/lib/python3.12/site-packages/pyannote/audio/core/pipeline.py", line 326, in __call__
    return self.apply(file, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/mio256/pyannote_audio/venv/lib/python3.12/site-packages/pyannote/audio/pipelines/speaker_diarization.py", line 578, in apply
    discrete_diarization = self.reconstruct(
                           ^^^^^^^^^^^^^^^^^
  File "/Users/mio256/pyannote_audio/venv/lib/python3.12/site-packages/pyannote/audio/pipelines/speaker_diarization.py", line 403, in reconstruct
    clustered_segmentations = np.NAN * np.zeros(
                              ^^^^^^
  File "/Users/mio256/pyannote_audio/venv/lib/python3.12/site-packages/numpy/__init__.py", line 410, in __getattr__
    raise AttributeError("module {!r} has no attribute "
AttributeError: module 'numpy' has no attribute 'NAN'. Did you mean: 'nan'?
(venv) FAIL
```

One of the solutions is to replace `np.NAN` with `np.nan`.

(for example, replace `np.NAN` with `np.nan` by VSCode's built-in replace function)
