import { TestBed } from '@angular/core/testing';

import { EnumParserService } from './enum-parser.service';

describe('EnumParserService', () => {
  let service: EnumParserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EnumParserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
