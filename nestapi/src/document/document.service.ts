import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Document } from './document.entity';

@Injectable()
export class DocumentService {
  constructor(
    @InjectRepository(Document)
    private documentRepository: Repository<Document>,
  ) {}

  async createDocument(data): Promise<Document> {
    return this.documentRepository.save(data);
  }

  async getDocument(id: string): Promise<Document> {
    return this.documentRepository.findOne(id);
  }

  async updateDocument(id: string, data): Promise<any> {
    return this.documentRepository.update(id, data);
  }

  async deleteDocument(id: string): Promise<any> {
    return this.documentRepository.delete(id);
  }
}
