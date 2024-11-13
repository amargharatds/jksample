import { Injectable, HttpService } from '@nestjs/common';
import { catchError, lastValueFrom } from 'rxjs';
import { AxiosResponse } from 'axios';

@Injectable()
export class IngestionService {
  private readonly pythonApiUrl = 'http://localhost:8000'; // Replace with your Python backend URL

  constructor(private readonly httpService: HttpService) {}

  /**
   * Trigger document ingestion by calling the Python backend.
   * @param documentId ID of the document
   * @param content Document content to ingest
   * @returns Ingestion initiation response from the Python API
   */
  async triggerIngestion(documentId: string, content: string): Promise<AxiosResponse<any>> {
    const url = `${this.pythonApiUrl}/api/ingest`;

    const data = {
      documentId,
      content,
    };

    try {
      const response = await lastValueFrom(
        this.httpService.post(url, data).pipe(
          catchError((error) => {
            throw new Error(`Ingestion failed: ${error.message}`);
          }),
        ),
      );
      return response.data;
    } catch (error) {
      console.error('Error triggering ingestion:', error);
      throw error;
    }
  }

  /**
   * Check the ingestion status by calling the Python backend.
   * @param documentId ID of the document to check status for
   * @returns Ingestion status from the Python API
   */
  async getIngestionStatus(documentId: string): Promise<AxiosResponse<any>> {
    const url = `${this.pythonApiUrl}/api/ingest/status/${documentId}`;

    try {
      const response = await lastValueFrom(
        this.httpService.get(url).pipe(
          catchError((error) => {
            throw new Error(`Failed to get ingestion status: ${error.message}`);
          }),
        ),
      );
      return response.data;
    } catch (error) {
      console.error('Error fetching ingestion status:', error);
      throw error;
    }
  }
}
