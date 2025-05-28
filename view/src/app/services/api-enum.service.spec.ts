import { TestBed } from '@angular/core/testing';

import { ApiEnumService } from './api-enum.service';

describe('ApiEnumService', () => {
  let service: ApiEnumService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiEnumService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
