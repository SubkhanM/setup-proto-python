# Setup Proto Python with Backend & Frontend Integration

Proyek ini adalah sistem yang terdiri dari **backend**, **frontend**, dan **Protocol Buffers (Protobuf)** untuk komunikasi antar komponen. Protobuf digunakan untuk mendefinisikan struktur data dan mempermudah komunikasi antara backend dan frontend.

## 🛠️ Teknologi yang Digunakan
### Backend
- **Framework:** Flask/FastAPI/Django REST
- **Bahasa:** Python
- **Serialization:** Protobuf
- **Komunikasi:** gRPC atau REST API

### Frontend
- **Framework:** React/Angular/Vue
- **Bahasa:** JavaScript/TypeScript
- **State Management:** Redux/Context API (opsional)

### Protocol Buffers
- **Versi Protobuf:** 3.x.x atau lebih baru
- Digunakan untuk mendefinisikan pesan-pesan data.

---

## 🚀 Cara Menjalankan Proyek
### Prasyarat
1. **Python 3.8+**
2. **Node.js dan npm/yarn**
3. **Protocol Buffers Compiler (`protoc`)**

### Langkah 1: Clone Repositori
```bash
git clone (https://github.com/SubkhanM/setup-proto-python)
cd project
```
Langkah 2: Setup Protobuf untuk Python

    Pastikan protoc terinstal. Jika belum, unduh dari halaman resmi Protocol Buffers.
    Generate file Python dari file .proto:

cd proto
protoc --proto_path=. --python_out=../backend --grpc_python_out=../backend my_service.proto

Jika menggunakan frontend, generate file JavaScript:

    protoc --proto_path=. --js_out=import_style=commonjs,binary:../frontend/src my_service.proto

Langkah 3: Jalankan Backend

    Install dependencies:

cd backend
pip install -r requirements.txt
Jalankan server:

    python app.py

Langkah 4: Jalankan Frontend

    Install dependencies:

cd frontend
npm install

Jalankan server frontend:

    npm start

📜 Contoh Protobuf

File proto/my_service.proto:
```
syntax = "proto3";

package myservice;

// Definisi layanan
service MyService {
  rpc GetData (RequestMessage) returns (ResponseMessage);
}

// Pesan-pesan
message RequestMessage {
  string query = 1;
}

message ResponseMessage {
  string result = 1;
}
```
📤 Komunikasi Backend-Frontend
    Backend menggunakan file Protobuf yang telah di-generate untuk memproses permintaan gRPC.
    Frontend menggunakan binding JavaScript untuk serialisasi dan deserialisasi pesan Protobuf.
💻 Contoh Implementasi
Backend (Python)
File: backend/app.py
```
from concurrent import futures
import grpc
import my_service_pb2
import my_service_pb2_grpc

class MyServiceServicer(my_service_pb2_grpc.MyServiceServicer):
    def GetData(self, request, context):
        return my_service_pb2.ResponseMessage(result=f"Hello, {request.query}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

Frontend (React + JavaScript)

File: frontend/src/service.js

import { RequestMessage, ResponseMessage } from './my_service_pb';

export function sendRequest(query) {
  const request = new RequestMessage();
  request.setQuery(query);

  // Serialize to binary and send via gRPC/HTTP
  const binaryData = request.serializeBinary();
  // ...send binaryData to backend
}
```

# 📋 Lisensi
Proyek ini dilisensikan di bawah MIT License.

# 🤝 Kontribusi
Kontribusi sangat diterima! Silakan fork repositori ini dan ajukan pull request.

