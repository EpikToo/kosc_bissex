import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BissexHistoryComponent } from './bissex-history.component';

describe('BissexHistoryComponent', () => {
  let component: BissexHistoryComponent;
  let fixture: ComponentFixture<BissexHistoryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexHistoryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BissexHistoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
