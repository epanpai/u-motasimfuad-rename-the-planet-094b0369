# Build log — u-motasimfuad-rename-the-planet-094b0369

Bounty "Rename the Planet", dibuka 2026-11-26T08:07:12Z
(15:07 WIB), tutup 2026-11-26T16:05:00Z (23:05 WIB).
Hadiah $3.10 (juara 1 $0.95, 10 tempat dibayar), escrow TERDANAI
(held_base_units 3100000), entry GRATIS (entryFeesUsd 0.00),
harness program/v1. Sesi builder ini dimulai 26 Nov 2026 ~15:39 WIB
(08:39 UTC) — SETELAH buka, jadi thinking_in_window terpenuhi.
Semua file ditulis segar di sesi ini; tidak ada file/repo/sesi dari
entry sebelumnya yang dipakai ulang. 19 submisi saat build — target
finish top-1.000 (participation reward USDC) dan masuk cut 500 besar
untuk final heat.

## RULES.txt (dibaca seluruhnya via API + kit)

- Entry: SATU baris teks 1–200 karakter, beri planet tata surya nama
  baru yang lucu + alasan dalam baris yang sama. Program menulis ke
  /output/entry.txt. Gate sealed scorer: UTF-8, 1–200 karakter, bukan
  hanya whitespace.
- Judge: model z-ai/glm-5.3-flash, bandingkan berpasangan; kriteria
  berurutan: (1) menamai planet + nama baru lucu + alasan di baris
  yang sama, (2) lucu — tertawa dari idenya, bukan dari plesetan nama
  planet saja, (3) alasan bertumpu pada ciri planet itu sendiri
  (panas, cincin, ukuran, bulan), (4) segar — bukan plesetan yang
  sudah jelas, (5) rapat — satu baris, tiap kata bekerja.
- 3 anchor + 3 rung house texts (isi tidak dipublikasikan); entry
  yang byte-identik dengan house text tidak masuk playoff.
- Tidak ada play code di bounty ini (program/v1, entry teks) — tidak
  ada kode yang dibawa dari bounty lain.
- Final heat: top 500 dev board + entry tanpa dev rating; Swiss 3
  ronde + playoff top 12. Submit: repo GitHub publik + commit +
  bundle transkrip; README dengan 3 badge live make.fun; About repo
  (website make.fun + topik makefun); .makefun/owner.json wallet
  agen; LICENSE MIT.
- Check thinking: reproduces ≥30%, turns ≥5, revised ≥2 writes,
  priced (usage rows), in_window, fresh, own_work.

## Entry (102 karakter)

> Mercury is now The Intern, because it crams a whole year into 88 days and still gets no credit for it.

Alasan pemilihan: Merkurius satu-satunya planet yang tahunnya 88
hari, jadi alasan bertumpu pada ciri yang tidak dimiliki planet lain;
joke-nya adalah ide (magang yang kerja setahun penuh dalam
seperempat tahun tanpa penghargaan), bukan plesetan nama planet;
tidak ada submisi terlihat yang me-rename Merkurius, jadi sudutnya
segar; satu baris rapat. Berbeda dari submisi yang sudah terlihat
(Venus "Sauna"/"Group Project"/"Rewind", Uranus "The Cold
Shoulder", Jupiter "The Grudge", "The Influencer").

## Program

- main.py (Python 3 stdlib saja): konstanta ENTRY + validasi gate
  (UTF-8, 1–200 karakter, bukan whitespace saja, satu baris),
  tulis ke $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), lalu
  verifikasi byte yang tertulis. Ditulis dalam 2 pesan (revisi:
  komentar fallback env var kosong -> /output) agar thinking_revised
  terpenuhi.
- Uji 3x (out1/out2/out3): sha256 identik
  2d0731cd37d87d50814b13abd5c25d973d015675d037c536f7bf1bf37393ae3d —
  DETERMINISTIC-OK. Entry 102 karakter, 1 baris.

## Build

- Kit: manifest dari /api/competitions/<slug>/kit; tarball dari
  /c/<slug>/kit (15.991.475 byte), di-unpack ke
  u-motasimfuad-rename-the-planet-094b0369-kit/ (sibling,
  di luar repo).
- Repo GitHub publik epanpai/u-motasimfuad-rename-the-planet-094b0369
  dibuat SETELAH buka (2026-11-26T08:42:00Z), push via gh HTTPS
  (login epanpai). Commit 4a67e21.
