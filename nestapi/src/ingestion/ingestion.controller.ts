import { Controller, Post, Body, HttpService } from '@nestjs/common';

@Controller('ingestion')
export class IngestionController {
  constructor(private readonly httpService: HttpService) {}

  @Post('/trigger')
  async triggerIngestion(@Body() data: { documentId: string, content: string }) {
    try {
      const response = await this.httpService.post('http://localhost:8000/api/v1/ingest/', data).toPromise();
      return response.data;
    } catch (error) {
      throw new Error('Error triggering ingestion');
    }
  }
}
